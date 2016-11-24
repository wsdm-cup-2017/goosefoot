import os
from src import definitions


def calculate_similarities(filename, method, inputType):
    with open(os.path.join(definitions.TRAINING_DIR, filename), mode='r', encoding='utf8') as trainfile:
        total_error = 0;
        for index, line in enumerate(trainfile):
            splitted = line.rstrip().split('	')
            person_name = splitted[0]
            variable = splitted[1]
            real_value = float(splitted[2])
            feature_value = method(person_name, variable, inputType)
            error_value = abs(real_value - feature_value)
            total_error += error_value
            print("{4:.2f} err: {0} - {1}: {2:.2f}-{3:.2f} (Real-Feature)".format(person_name, variable, real_value, feature_value, error_value))

        print("----- TOTAL ERROR: {0:.2f} -----".format(total_error / (index+1)))