import os
from . import persons

with open('../../../../_DATA/nomenclatures/persons.txt', encoding='utf8', mode='r') as fr:
    with open('../../../../_DATA/nomenclatures/missing_persons.txt', encoding='utf8', mode='w') as fw:
        for line in fr:
            person_name = line.split('	', 1)[0]
            modified_name = persons.remove_spaces(person_name)
            # Important: Change!
            file_name = 'D:/WSDM_Persons/persons/' + modified_name + '.txt'
            if not os.path.isfile(file_name):
                fw.write(person_name + "\n")
            elif os.path.getsize(file_name) < 200:
                with open(file_name, encoding='utf8', mode='r') as person_file:
                    for line in person_file:
                        if 'may refer to' in line:
                            print(modified_name)
                            break

