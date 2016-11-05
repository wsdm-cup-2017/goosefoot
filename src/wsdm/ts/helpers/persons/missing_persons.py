import os
from src.wsdm.ts.helpers.persons import persons
from definitions import NOMENCLATURES_DIR
from definitions import PERSONS_DIR

if __name__ == '__main__':
    with open(os.path.join(NOMENCLATURES_DIR, "persons.txt"), encoding='utf8', mode='r') as fr:
        with open(os.path.join(NOMENCLATURES_DIR, "missing_persons.txt"), encoding='utf8', mode='w') as fw:
            for line in fr:
                person_name = line.split('	', 1)[0]
                modified_name = persons.remove_spaces(person_name)
                file_name = os.path.join(PERSONS_DIR, modified_name + '.txt')
                if not os.path.isfile(file_name):
                    fw.write(line)

