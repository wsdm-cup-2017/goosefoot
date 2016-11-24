import sys

import definitions as definitions
import wsdm.ts.main.Config as Config
from wsdm.ts.helpers.nationalities import nationalities

from wsdm.ts.features import generalFeature
from wsdm.ts.features import word2VecFeature
from wsdm.ts.features import tfIdfFeature
from wsdm.ts.features import regressionFeature


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
        print("No file", person)
        return definitions.DEFAULT_SIMILARITY

    if generalFeature.is_positive(person, term, inputType):
        print("Positive", person, term)
        return definitions.MAX_SIMILARITY

    if generalFeature.is_negative(person, term, inputType):
        print("Negative", person, term)
        return definitions.MIN_SIMILARITY

    tfidif_similarity = tfIdfFeature.find_similarity(person, term, inputType)
    word2vec_similarity = word2VecFeature.find_similarity(person, term, inputType)
    regression_similarity = regressionFeature.find_similarity(person, term, inputType)

    print("%.2f" % regression_similarity, person, term)

    return regression_similarity


def main(argv):
    inputFile, outputFile = Config.getIOFiles(argv)
    inputType = check_file_content_type(inputFile)

    print('Load word2Vec model')
    word2VecFeature.load_module()
    print('Load regression models')
    regressionFeature.load_modules(word2VecFeature)

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

                if index % 1000 == 0:
                    print("\t".join([str(index), "%.2f" % score]))
                    
                inputFW.write("{0}	{1}	{2}\n".format(person, term, score))


if __name__ == '__main__':
    '''
    For unit test purposes, main can be called with arguments, different than sys.argv, e.g.:

    main(['-i','D:/eclipse/workspaces/wsdm_2017/triple-scoring/goosefoot/_DATA/test_sets/nationality.kb','-o' 'D:/temp/asd.txt'])'''

    main(sys.argv[1:])


