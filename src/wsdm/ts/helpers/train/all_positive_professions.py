import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.professions.professions as prof_lib
import src.wsdm.ts.helpers.train.common_train as common_train

def init_all_positive_professions():
    global persons

    result = common_train.init_professions_empty_dict()

    total_count = 0
    for person in persons:
        total_count += 1
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
                    print(total_count, mentioned_professions[0], person)
    return result


def save_all_positive_train_data(positive_dict, train_file):
    positive_lines = common_train.get_train_lines(positive_dict, True)

    with open(train_file, encoding='utf8', mode='w') as fw:
        for l in positive_lines:
            fw.write(l + "\n")


if __name__ == '__main__':
    persons = common_train.init_persons()
    all_positive_professions = init_all_positive_professions()
    save_all_positive_train_data(all_positive_professions, os.path.join(definitions.TRAINING_DIR, "all_positive_profession.train"))

