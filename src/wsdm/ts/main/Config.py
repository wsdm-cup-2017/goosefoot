import getopt


def getIOFiles(argv):
    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv, "i:o:")
    except getopt.GetoptError:
        print('Incorrect arguments. Please provide values for input and output file paths (-i <inputFile> -o <outputFile>)')
        return
    for opt, arg in opts:
        if opt == '-i':
            inputFile = arg
        elif opt == '-o':
            outputFile = arg
    return inputFile, outputFile
