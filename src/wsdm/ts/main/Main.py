import sys

import definitions
import src.wsdm.ts.main.Config as Config
from src.wsdm.ts.helpers.nationalities import nationalities

from src.wsdm.ts.features import generalFeature
from src.wsdm.ts.features import word2VecFeature
from src.wsdm.ts.features import tfIdfFeature

DEFAULT_VALUE = 3
MAX_VALUE = 7
MIN_VALUE = 0

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
        return DEFAULT_VALUE

    if generalFeature.is_positive(person, term, inputType):
        return MAX_VALUE

    if generalFeature.is_negative(person, term, inputType):
        return MIN_VALUE

    return DEFAULT_VALUE


def main(argv):
    inputFile, outputFile = Config.getIOFiles(argv)
    inputType = check_file_content_type(inputFile)

    with open(inputFile, encoding='utf8', mode='r') as inputFR:
        with open(outputFile, encoding='utf8', mode='w') as inputFW:
            for line in inputFR:
                splitted = line.split('\t')
                assert len(splitted) == 2, "Invalid input row"
                person = splitted[0]
                term = splitted[1]
                score = get_score(person, term, inputType)
                inputFW.write("{0}	{1}	{2}\n".format(person, term, score))


if __name__ == '__main__':
    '''
    For unit test purposes, main can be called with arguments, different than sys.argv, e.g.:

    main(['-i','D:/eclipse/workspaces/wsdm_2017/triple-scoring/goosefoot/_DATA/test_sets/nationality.kb','-o' 'D:/temp/asd.txt'])'''

    main(sys.argv[1:])



