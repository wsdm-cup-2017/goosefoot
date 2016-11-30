import sys

import definitions as definitions
import getopt
import ntpath
from wsdm.ts.helpers.nationalities import nationalities

from wsdm.ts.features import generalFeature
from wsdm.ts.features import word2VecFeature
from wsdm.ts.features import word_countFeature
from wsdm.ts.features import regressionFeature


def get_io_files(argv):
    inputFiles = []
    outputDir = ''
    try:
        opts, args = getopt.getopt(argv, "i:o:")
    except getopt.GetoptError:
        print('Incorrect arguments. Please provide values for input and output file paths (-i <inputFile> -o <outputFile>)')
        return
    for opt, arg in opts:
        if opt == '-i':
            inputFiles.append(arg)
        elif opt == '-o':
            outputDir = arg


    return list(
        (inputFile, "{0}/{1}".format(outputDir, ntpath.basename(inputFile)))
        for inputFile in inputFiles
    )

''' Returns the content type in the corresponding file (PERSON or NATIONALITY).'''
def check_file_content_type(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        profession_or_nationality = first_line.split('\t')[1]
        f.close()

    if profession_or_nationality.strip() in nationalities.nationalities_dict.values():
        return definitions.TYPE_NATIONALITY
    return definitions.TYPE_PROFESSION


def get_score(person, term, inputType):
    if not generalFeature.has_file(person):
        # print("No file", person)
        return definitions.DEFAULT_SIMILARITY

    if generalFeature.is_positive(person, term, inputType):
        # print("Positive", person, term)
        return definitions.MAX_SIMILARITY

    if generalFeature.is_negative(person, term, inputType):
        # print("Negative", person, term)
        return definitions.MIN_SIMILARITY

    regression_similarity = regressionFeature.find_similarity(person, term, inputType)
    word_count_similarity = word_countFeature.find_similarity(person, term, inputType)

    score = definitions.REGRESSION_MULTIPLIER * regression_similarity \
                + definitions.WORD_COUNT_MULTIPLIER * word_count_similarity

    '''
    print('\t'.join("%.2f" % score for score in [
        word2VecFeature.find_similarity(person, term, inputType),
        tfIdfFeature.find_similarity(person, term, inputType),
        word_countFeature.find_similarity(person, term, inputType),
        regressionFeature.find_similarity(person, term, inputType),
        score
    ]))

    print("%.2f" % regression_similarity, person, term)
    '''

    return score


def process(inputFile, outputFile):
    inputType = check_file_content_type(inputFile)

    with open(inputFile, encoding='utf8', mode='r') as inputFR:
        with open(outputFile, encoding='utf8', mode='w') as inputFW:
            index = 0
            for line in inputFR:
                index +=1
                splitted = line.rstrip().split('\t')
                assert len(splitted) == 2, "Invalid input row"
                person = splitted[0]
                term = splitted[1]
                score = get_score(person, term, inputType)

                '''
                if index % 1000 == 0:
                    print("\t".join([str(index), "%.2f" % score]))
                '''
                    
                inputFW.write("{0}	{1}	{2}\n".format(person, term, "%.0f" % score))


if __name__ == '__main__':
    print('Load word2Vec model')
    word2VecFeature.load_module()
    print('Load regression models')
    regressionFeature.load_modules(word2VecFeature)

    for inputFile, outputFile in get_io_files(sys.argv[1:]):
        process(inputFile, outputFile)



