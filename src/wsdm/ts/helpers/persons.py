import re

def process_splitted(splitted, person_name, alternative_names):
    for index, word in enumerate(splitted):
        if (splitted[index] in alternative_names):
            splitted[index] = person_name

    i = 1
    while i < len(splitted):
        if splitted[i] == splitted[i - 1]:
            splitted.pop(i)
            i -= 1
        i += 1

    return splitted

def remove_spaces(person):
    return person.replace('"', "_").replace(" ", "_").replace("/","_")

def split_to_names(person):
    return person.replace("_", " ")

def get_persons_names(first_line, person_name):
    splitted = first_line.split('(')
    if splitted:
        full_name = splitted[0].strip()
        return full_name.split(' ')
    else:
        return split_to_names(person_name)

