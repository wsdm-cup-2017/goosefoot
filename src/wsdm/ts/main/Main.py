import sys
import Config


def main(argv):
    inputFile, outputFile = Config.getIOFiles(argv)
    print('Input file is: ', inputFile)
    print('Output file is: ', outputFile)

if __name__ == '__main__':
    main(sys.argv[1:])

