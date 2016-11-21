import re
from wsdm.ts.helpers.persons.common import split_to_words

def process_splitted(splitted, person_name, alternative_names):
    for index, word in enumerate(splitted):
        if splitted[index] in alternative_names and len(splitted[index]) > 1:
            # print(splitted[index], ' -> ', person_name)
            splitted[index] = person_name

    i = 1
    while i < len(splitted):
        if splitted[i] == splitted[i - 1]:
            splitted.pop(i)
            i -= 1
        i += 1

    return splitted

def remove_spaces(person):
    return person.replace('"', "_")\
        .replace(" ", "_")\
        .replace("/","_")\
        .replace("*","_")

def add_spaces(person):
    return person.replace("_", " ")

def get_persons_names(first_line, person_name):
    splitted = first_line.split('(')
    if len(splitted) > 1:
        full_name = splitted[0].strip()
        return split_to_words(full_name)
    else:
        full_name = add_spaces(person_name)
        return split_to_words(full_name)

