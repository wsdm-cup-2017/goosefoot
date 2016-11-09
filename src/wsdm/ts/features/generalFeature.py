import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.train.common_train as common_train

def has_file(person):
    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
    return os.path.isfile(person_file)


def is_nationality_negative(person, nationality):
    return common_train.is_nationality_negative(person, nationality)


def is_profession_negative(person, profession):
    return common_train.is_profession_negative(person, profession)


def is_nationality_positive(person, nationality):
    positive_nationality = common_train.get_positive_nationality(person)
    return nationality == positive_nationality


def is_profession_positive(person, profession):
    positive_profession = common_train.get_positive_profession(person)
    return profession == positive_profession
