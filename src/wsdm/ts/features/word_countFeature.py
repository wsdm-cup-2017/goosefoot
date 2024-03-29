import wsdm.ts.helpers.persons.persons as p_lib
import definitions
import sys

import re
import numpy as np
import os

def find_similarity(person_name, term, inputType):
    result={}
    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person_name) + ".txt")
    if os.path.isfile(person_file):
        with open(person_file, 'r', encoding='utf8') as f:
            if inputType == definitions.TYPE_NATIONALITY:
                result = get_person_nationalities(f)
            elif inputType == definitions.TYPE_PROFESSION:
                result = get_person_professions(f)
            else:
                raise TypeError

    if (term in result.keys()):
        return result[term]

    return 0

def remove_quoted_words(text):
    text=text.lower()
    #quoted_word_pattern = re.compile(r"'([a-z]\w*)'")
    result = re.findall(r"\".*?\"", text)
    for word in result:
        text=text.replace(word,'')
    return text


def get_person_professions(file):
    result={}
    profession_majority = 7

    file_content = file.read().lower()
    file_content = remove_quoted_words(file_content)
    profession_indexes = {}

    with open(os.path.join(definitions.NOMENCLATURES_DIR, "professions.txt"), encoding='utf8', mode='r') as fr:
        for profession_line in fr:
            profession = profession_line.rstrip()
            profession_lower = profession.lower()
            profession_words = profession_lower.split(' ')

            if profession_lower in file_content:
                profession_indexes[profession] = file_content.index(profession_lower)
            elif len(profession_words) > 1 and all(word in file_content for word in profession_words):
                profession_indexes[profession] = np.mean([file_content.index(word) for word in profession_words])

    for profession in sorted(profession_indexes, key=profession_indexes.get):
        result[profession] = profession_majority
        if profession_majority > 0:
            profession_majority -= 1

        if profession_majority <= 0:
            break

    return result

def get_person_nationalities(file):
    result={}
    nationality_majority = 7
    from wsdm.ts.helpers.nationalities import nationalities
    for line in file:
        nationality_indexes = {}
        for person, nationality in nationalities.nationalities_dict.items():
            line = line.replace(person, nationality)

        with open(os.path.join(definitions.NOMENCLATURES_DIR, "nationalities.txt"), encoding='utf8', mode='r') as fr:
            for nationality_line in fr:
                nationality = nationality_line.rstrip()
                if nationality not in result:
                    if nationality in line:
                        nationality_indexes[nationality] = line.index(nationality)

        if len(nationality_indexes) > 0:
            for nationality in sorted(nationality_indexes, key=nationality_indexes.get):
                result[nationality] = nationality_majority
                if nationality_majority > 0:
                    nationality_majority-=1

        if nationality_majority <= 0:
            break

    return result


def main(argv):
    #f = codecs.open('D:/education/FMI_Sofia_University/III_sem/wsdm_2017/data/DATA_2016_10_15/persons/Richard_Séguin.txt', 'r', encoding='utf8')
    #result = get_person_nationalities(f)
    print(find_similarity('Richard Séguin', 'Germany', definitions.TYPE_NATIONALITY))
    #f.close()
    #print(result)

if __name__ == '__main__':
    main(sys.argv[:])