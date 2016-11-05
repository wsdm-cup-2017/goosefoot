import random
import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.countries.countries as c_lib
import src.wsdm.ts.helpers.professions.professions as prof_lib
import src.wsdm.ts.helpers.train.common_train as common_train

NEGATIVE_EXAMPLES_COUNT = 10
persons = common_train.init_persons()

def init_negative_countries():
    global persons

    result = common_train.init_countries_empty_dict()
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
                        print(country, person)

    return result

def init_positive_countries():
    global persons

    result = common_train.init_countries_empty_dict()

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
                    print(total_count, mentioned_countries[0], person)
    return result

def init_negative_professions():
    global persons

    result = common_train.init_professions_empty_dict()
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
                        print(profession, person)

    return result

def init_positive_professions():
    global persons

    result = common_train.init_professions_empty_dict()

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
                    print(total_count, mentioned_professions[0], person)
    return result


positive_countries = init_positive_countries()
negative_countries = init_negative_countries()
common_train.save_train_data(positive_countries, negative_countries, os.path.join(definitions.TRAINING_DIR, "custom_nationality.train"))

positive_professions = init_positive_professions()
negative_professions = init_negative_professions()
common_train.save_train_data(positive_professions, negative_professions, os.path.join(definitions.TRAINING_DIR, "custom_profession.train"))

