import os

import definitions
from definitions import NOMENCLATURES_DIR
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.nationalities.nationalities as nat_lib
import src.wsdm.ts.helpers.professions.professions as prof_lib

def init_persons():
    persons = []

    with open(os.path.join(NOMENCLATURES_DIR, "persons.txt"), encoding='utf8') as persons_f:
        for line in persons_f:
            persons.append(line.split('	', 1)[0])

    return persons


def get_train_lines(dict, is_positive):
    score = "7" if is_positive else "0"
    result = []
    for key, val in dict.items():
        if len(val) > 0:
            for item in val:
                result.append("{0}	{1}	{2}".format(item, key, score))
    return result

def save_train_data(positive_dict, negative_dict, train_file):
    positive_lines = get_train_lines(positive_dict, True)
    negative_lines = get_train_lines(negative_dict, False)

    with open(train_file, encoding='utf8', mode='w') as fw:
        for (pl, nl) in zip(positive_lines, negative_lines):
            fw.write(pl + "\n")
            fw.write(nl + "\n")

def init_nationalities_empty_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "nationalities.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            nationality = line.rstrip()
            result[nationality] = []

    return result

def init_professions_empty_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "professions.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            profession = line.rstrip()
            result[profession] = []

    return result


def is_nationality_negative(person, nationality):
    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
    if os.path.isfile(person_file):
        with open(person_file, 'r', encoding='utf8') as fr:
            content = fr.read()
            for synonym, coun in nat_lib.nationalities_dict.items():
                content = content.replace(synonym, coun)

            if nationality in content:
                return False

    return True


def is_profession_negative(person, profession):
    similarity_words = prof_lib.get_similarity_words(profession)
    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
    if os.path.isfile(person_file):
        with open(person_file, 'r', encoding='utf8') as fr:
            content = fr.read()
            if any(x in content for x in similarity_words):
                return False

    return True
