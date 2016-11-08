import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.nationalities.nationalities as nat_lib
import src.wsdm.ts.helpers.train.common_train as common_train

def init_all_positive_nationalities():
    global persons

    result = common_train.init_nationalities_empty_dict()
    total_count = 0
    for person in persons:
        total_count += 1
        positive_nationality = common_train.get_positive_nationality(person)
        if positive_nationality != None:
            result[positive_nationality].append(person)
            print(total_count, positive_nationality, person)

    return result


def save_all_positive_train_data(positive_dict, train_file):
    positive_lines = common_train.get_train_lines(positive_dict, True)

    with open(train_file, encoding='utf8', mode='w') as fw:
        for l in positive_lines:
            fw.write(l + "\n")


if __name__ == '__main__':
    persons = common_train.init_persons()
    all_positive_nationalities = init_all_positive_nationalities()
    save_all_positive_train_data(all_positive_nationalities, os.path.join(definitions.TRAINING_DIR, "all_positive_nationality.train"))

