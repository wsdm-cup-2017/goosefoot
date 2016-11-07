import random
import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.nationalities.nationalities as nat_lib
import src.wsdm.ts.helpers.professions.professions as prof_lib
import src.wsdm.ts.helpers.train.common_train as common_train

NEGATIVE_EXAMPLES_COUNT = 10
persons = common_train.init_persons()

def init_negative_nationalities():
    global persons

    result = common_train.init_nationalities_empty_dict()
    for nationality in result:
        while len(result[nationality]) < NEGATIVE_EXAMPLES_COUNT:
            person = random.choice(persons)

            if person not in result[nationality] and common_train.is_nationality_negative(person, nationality):
                result[nationality].append(person)
                print(nationality, person)

    return result

def init_positive_nationalities():
    global persons

    result = common_train.init_nationalities_empty_dict()

    total_count = 0
    while total_count < len(result) * NEGATIVE_EXAMPLES_COUNT:
        person = random.choice(persons)
        person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
        if os.path.isfile(person_file):
            with open(person_file, 'r', encoding='utf8') as fr:
                first_line = fr.readline().split(".")[0]
                for synonym, coun in nat_lib.nationalities_dict.items():
                    first_line = first_line.replace(synonym, coun)

                mentioned_nationalities = tuple(temp_nationality for temp_nationality in result  if temp_nationality in first_line)
                if len(mentioned_nationalities) == 1 and person not in result[mentioned_nationalities[0]]:
                    result[mentioned_nationalities[0]].append(person)
                    total_count += 1
                    print(total_count, mentioned_nationalities[0], person)
    return result

def init_negative_professions():
    global persons

    result = common_train.init_professions_empty_dict()
    for profession in result:
        similarity_words = prof_lib.get_similarity_words(profession)
        while len(result[profession]) < NEGATIVE_EXAMPLES_COUNT:
            person = random.choice(persons)
            if person not in result[profession] and common_train.is_profession_negative(person, profession):
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


if __name__ == '__main__':
    positive_nationalities = init_positive_nationalities()
    negative_nationalities = init_negative_nationalities()
    common_train.save_train_data(positive_nationalities, negative_nationalities, os.path.join(definitions.TRAINING_DIR, "custom_nationality.train"))

    positive_professions = init_positive_professions()
    negative_professions = init_negative_professions()
    common_train.save_train_data(positive_professions, negative_professions, os.path.join(definitions.TRAINING_DIR, "custom_profession.train"))

