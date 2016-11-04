import os
import random
from definitions import NOMENCLATURES_DIR
from definitions import TRAINING_DIR
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.countries.countries as c_lib
import src.wsdm.ts.helpers.professions.professions as prof_lib

NEGATIVE_EXAMPLES_COUNT = 10
persons = []

def init_persons():
    global persons

    with open(os.path.join(NOMENCLATURES_DIR, "persons.txt"), encoding='utf8') as persons_f:
        for line in persons_f:
            persons.append(line.split('	', 1)[0])

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


def init_countries_empty_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "nationalities.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            country = line.rstrip()
            result[country] = []

    return result

def init_professions_empty_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "professions.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            profession = line.rstrip()
            result[profession] = []

    return result

def init_professions_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "professions.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            country = line.rstrip()
            result[country] = []

    return result

def init_negative_countries():
    global persons

    result = init_countries_empty_dict()
    for country in result:
        while len(result[country]) < NEGATIVE_EXAMPLES_COUNT:
            person = random.choice(persons)
            person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
            if os.path.isfile(person_file):
                with open(person_file, 'r', encoding='utf8') as fr:
                    content = fr.read()
                    for synonym, coun in c_lib.countries_dict.items():
                        content = content.replace(synonym, coun)

                    if not country in content:
                        result[country].append(person)
                        # print(country, person)

    return result

def init_positive_countries():
    global persons

    result = init_countries_empty_dict()

    total_count = 0
    while total_count < len(result) * NEGATIVE_EXAMPLES_COUNT:
        person = random.choice(persons)
        person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
        if os.path.isfile(person_file):
            with open(person_file, 'r', encoding='utf8') as fr:
                first_line = fr.readline().split(".")[0]
                for synonym, coun in c_lib.countries_dict.items():
                    first_line = first_line.replace(synonym, coun)

                mentioned_countries = tuple(temp_country for temp_country in result  if temp_country in first_line)
                if len(mentioned_countries) == 1 and person not in result[mentioned_countries[0]]:
                    result[mentioned_countries[0]].append(person)
                    total_count += 1
                    # print(total_count, mentioned_countries[0], person)
    return result

def init_negative_professions():
    global persons

    result = init_professions_empty_dict()
    for profession in result:
        similarity_words = prof_lib.get_similarity_words(profession)
        while len(result[profession]) < NEGATIVE_EXAMPLES_COUNT:
            person = random.choice(persons)
            person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
            if os.path.isfile(person_file):
                with open(person_file, 'r', encoding='utf8') as fr:
                    content = fr.read()
                    if not any(x in content for x in similarity_words):
                        result[profession].append(person)
                        # print(profession, person)

    return result

def init_positive_professions():
    global persons

    result = init_professions_empty_dict()

    total_count = 0
    while total_count < len(result) * NEGATIVE_EXAMPLES_COUNT:
        person = random.choice(persons)
        person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
        if os.path.isfile(person_file):
            with open(person_file, 'r', encoding='utf8') as fr:
                first_line = fr.readline().split(".")[0]
                mentioned_professions = []

                for profession in result:
                    similarity_words = prof_lib.get_similarity_words(profession)
                    if all(x in first_line for x in similarity_words):
                        mentioned_professions.append(profession)

                if len(mentioned_professions) == 1 and person not in result[mentioned_professions[0]]:
                    result[mentioned_professions[0]].append(person)
                    total_count += 1
                    # print(total_count, mentioned_professions[0], person)
    return result


init_persons()

positive_countries = init_positive_countries()
negative_countries = init_negative_countries()
save_train_data(positive_countries, negative_countries, os.path.join(definitions.TRAINING_DIR, "custom_nationality.train"))

positive_professions = init_positive_professions()
negative_professions = init_negative_professions()
save_train_data(positive_professions, negative_professions, os.path.join(definitions.TRAINING_DIR, "custom_profession.train"))

