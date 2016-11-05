import sys
import Config


from src.wsdm.ts.helpers.countries import countries

''' Returns the content type in the corresponding file (PERSON or NATIONALITY).'''
def check_file_content_type(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        profession_or_nationality = first_line.split('\t')[1]
        f.close()

    if profession_or_nationality.lower().strip() in countries.countries_dict.values():
        return 'NATIONALITY'
    return 'PROFESSION'



def main(argv):

    inputFile, outputFile = Config.getIOFiles(argv)
    print('Input file is: ', inputFile)
    print('Output file is: ', outputFile)
    print('Content type is: ' + check_file_content_type(inputFile))



if __name__ == '__main__':
    '''
    For unit test purposes, main can be called with arguments, different than sys.argv, e.g.:

    main(['-i','D:/eclipse/workspaces/wsdm_2017/triple-scoring/goosefoot/_DATA/test_sets/nationality.kb','-o' 'D:/temp/asd.txt'])'''

    main(sys.argv[1:])



