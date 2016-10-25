import os
import random
from definitions import NOMENCLATURES_DIR
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.countries.countries as c_lib

NEGATIVE_EXAMPLES_COUNT = 10
persons = []

def init_persons():
    global persons

    with open(os.path.join(NOMENCLATURES_DIR, "persons.txt"), encoding='utf8') as persons_f:
        for line in persons_f:
            persons.append(line.split('	', 1)[0])


def init_countries_empty_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "nationalities.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            country = line.rstrip()
            result[country] = []

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

    return result

def init_positive_countries():
    global persons

    result = init_countries_empty_dict()

    total_count = 0
    while total_count < 1000:
        person = random.choice(persons)
        person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
        if os.path.isfile(person_file):
            with open(person_file, 'r', encoding='utf8') as fr:
                first_line = fr.readline()
                for synonym, coun in c_lib.countries_dict.items():
                    first_line = first_line.replace(synonym, coun)

                mentioned_countries = tuple(temp_country for temp_country in result  if temp_country in first_line)
                if len(mentioned_countries) == 1 and person not in result[mentioned_countries[0]]:
                    result[mentioned_countries[0]].append(person)
                    total_count += 1
                    print(total_count, mentioned_countries[0], person)



    return result


init_persons()

negative_countries = init_negative_countries()
positive_countries = init_positive_countries()

print(positive_countries["Bulgaria"])
