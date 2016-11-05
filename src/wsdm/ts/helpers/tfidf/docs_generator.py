import os
from definitions import NOMENCLATURES_DIR
from definitions import PROFESSIONS_DIR
from definitions import TRAINING_DIR
from definitions import TFIDF_PROFESSIONS_DIR
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib


def init_dictionary():
    professions = {}
    with open(os.path.join(NOMENCLATURES_DIR, 'professions.txt'), encoding='utf8', mode='r') as f:
        for line in f:
            profession = line.rstrip()
            with open(os.path.join(PROFESSIONS_DIR, profession + '.txt'), encoding='utf8', mode='r') as prof_file:
                professions[profession] = prof_file.read()
    return professions

def add_training_data(professions):
    with open(os.path.join(TRAINING_DIR, 'all_positive_profession.train'), encoding='utf8', mode='r') as f:
        for i, line in enumerate(f):
            splitted = line.rstrip().split('	')
            person = splitted[0]
            profession = splitted[1]

            with open(os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt"), 'r', encoding='utf8') as pf:
                professions[profession] += "\n" + pf.read()
                print(i, person)

def write_files(professions):
    for profession, text in professions.items():
        with open(os.path.join(TFIDF_PROFESSIONS_DIR, "tfidf_professions", profession + ".txt"), encoding='utf8', mode='x') as f:
            f.write(text)

def main():
    professions = init_dictionary()
    add_training_data(professions)
    write_files(professions)
