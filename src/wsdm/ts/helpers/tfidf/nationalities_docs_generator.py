import os
from definitions import NOMENCLATURES_DIR
from definitions import TRAINING_DIR
from definitions import TFIDF_NATIONALITIES_DIR
import definitions
import wsdm.ts.helpers.persons.persons as p_lib

def init_dictionary():
    nationalities = {}
    with open(os.path.join(NOMENCLATURES_DIR, 'nationalities.txt'), encoding='utf8', mode='r') as f:
        for line in f:
            nationality = line.rstrip()
            nationalities[nationality] = ""
    return nationalities

def add_training_data(nationalities):
    with open(os.path.join(TRAINING_DIR, 'all_positive_nationality.train'), encoding='utf8', mode='r') as f:
        for i, line in enumerate(f):
            splitted = line.rstrip().split('	')
            person = splitted[0]
            nationality = splitted[1]

            with open(os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt"), 'r', encoding='utf8') as pf:
                nationalities[nationality] += pf.read() + "\n"
                print(i, person)

def write_files(nationalities):
    for nationality, text in nationalities.items():
        with open(os.path.join(TFIDF_NATIONALITIES_DIR, nationality + ".txt"), encoding='utf8', mode='x') as f:
            f.write(text)

def main():
    nationalities = init_dictionary()
    add_training_data(nationalities)
    write_files(nationalities)


if __name__ == '__main__':
    main()
