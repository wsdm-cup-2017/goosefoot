import src.wsdm.ts.helpers.persons.persons as p_lib
from src.wsdm.ts.helpers.tfidf.professions_tfidf_dictionary import PROFESSIONS_DICT
from src.wsdm.ts.helpers.tfidf.nationalities_tfidf_dictionary import NATIONALITIES_DICT
import os
import definitions
from collections import Counter
import operator
import nltk
import sys
import codecs
import re

def find_similarity(person_name, term, inputType):
    return ''

def custom_similarity(person, key, words_dict):
    result = -1
    #TODO implement !
    if result > 7:
        return 7

    return result


def find_similarity(person_name, term, inputType):
    if inputType == definitions.TYPE_NATIONALITY:
        dict = NATIONALITIES_DICT
    elif inputType == definitions.TYPE_PROFESSION:
        dict = PROFESSIONS_DICT
    else:
        raise TypeError

    return custom_similarity(person_name, term, dict)


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

    #if the exact profession is found return 7
    #and continue
    for profession in professions.profession_synonyms_map.keys():
        #get the first two rows from the file
        overview_line = lines[0] + lines[1] + lines[2]
        line_words = nltk.word_tokenize(overview_line.lower())
        if (profession in line_words):
            result[profession] = profession_majority
            profession_majority-=1

    for line in lines:
        line = remove_quoted_words(line)

        words = nltk.word_tokenize(line.lower())

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

                if (profession_first_word == word or '''profession_last_word''' == word) and (profession not in result):
                    result[profession] = profession_majority
                    if profession_majority > 0:
                        profession_majority-=1

    return result

def get_person_nationalities(file):
    result={}
    lines = file.readlines()
    nationality_majority = 7
    from wsdm.ts.helpers.nationalities import nationalities
    for line in lines:
        words = nltk.word_tokenize(line.lower())
        for person, country in nationalities.nationalities_dict.items():
            if (country not in result) and ((person in line) or (country in line)):
                result[country] = nationality_majority
                if nationality_majority > 0:
                    nationality_majority-=1
    return result


def main(argv):
    f = codecs.open('D:/education/FMI_Sofia_University/III_sem/wsdm_2017/data/DATA_2016_10_15/persons/Gowin_Knight.txt', 'r', encoding='utf8')
    result = get_person_nationalities(f)
    f.close()
    print(result)

if __name__ == '__main__':
    main(sys.argv[:])