import os
import definitions
import wsdm.ts.helpers.persons.persons as p_lib
import wsdm.ts.helpers.professions.professions as prof_lib
import wsdm.ts.helpers.train.common_train as common_train

def init_all_positive_professions():
    global persons

    result = common_train.init_professions_empty_dict()
    total_count = 0
    for person in persons:
        total_count += 1
        positive_profession = common_train.get_positive_profession(person)
        if positive_profession != None:
            result[positive_profession].append(person)
            print(total_count, positive_profession, person)

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

