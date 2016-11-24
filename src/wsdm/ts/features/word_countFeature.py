import src.wsdm.ts.helpers.persons.persons as p_lib
import definitions
import sys

import re
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


def refine_results(lines, initial_result):
    first_profession_word_map={}
    for line in lines:
        for profession in initial_result:
            profession_words = profession.split()
            if (profession_words[0] in line):
                if (profession_words[0] in first_profession_word_map):
                    first_profession_word_map[profession_words[0]] = first_profession_word_map[profession_words] + 1
                else:
                    first_profession_word_map[profession_words[0]] = 1
    #print(first_profession_word_map)
    return {}

def get_person_professions(file):
    result={}
    lines = file.readlines()
    profession_majority = 7
    from wsdm.ts.helpers.professions import professions

    for line in lines:
        #It`s important to remove all quoted strings as
        #this may cause problems when searching professions
        #or nationalities
        line = remove_quoted_words(line)

        words = p_lib.split_to_words(line.lower())

        for profession in professions.profession_synonyms_map.keys():
            profession_words = profession.split(' ')
            for word in words:
                profession_length = len(profession_words)
                profession_first_word = profession_words[0]
                profession_last_word = profession_words[0]

                if (profession_length == 2):
                    profession_last_word = profession_words[1]
                elif (profession_length > 2):
                    profession_first_word = profession_words[-2]
                    profession_last_word = profession_words[-1]
                     #'''or profession_last_word == word'''
                if (profession_first_word == word) and (profession not in result):
                    result[profession.lower()] = profession_majority
                    if profession_majority > 0:
                        profession_majority-=1

    return result

def get_person_nationalities(file):
    result={}
    lines = file.readlines()
    nationality_majority = 7
    from wsdm.ts.helpers.nationalities import nationalities
    for line in lines:
        for person, country in nationalities.nationalities_dict.items():
            if (country not in result) and ((person in line) or (country in line)):
                result[country.lower()] = nationality_majority
                if nationality_majority > 0:
                    nationality_majority-=1
    return result


def main(argv):
    #f = codecs.open('D:/education/FMI_Sofia_University/III_sem/wsdm_2017/data/DATA_2016_10_15/persons/Richard_Séguin.txt', 'r', encoding='utf8')
    #result = get_person_nationalities(f)
    print(find_similarity('Richard Séguin', 'Germany', definitions.TYPE_NATIONALITY))
    #f.close()
    #print(result)

if __name__ == '__main__':
    main(sys.argv[:])