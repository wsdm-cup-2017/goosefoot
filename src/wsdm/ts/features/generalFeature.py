import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib
import src.wsdm.ts.helpers.train.common_train as common_train

def has_file(person):
    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
    return os.path.isfile(person_file)


def is_negative(person, term, inputType):
    if inputType == definitions.TYPE_NATIONALITY:
        return common_train.is_nationality_negative(person, term)
    elif inputType == definitions.TYPE_PROFESSION:
        return common_train.is_profession_negative(person, term)
    else:
        raise TypeError


def is_positive(person, term, inputType):
    if inputType == definitions.TYPE_NATIONALITY:
        positive_item = common_train.get_positive_nationality(person)
    elif inputType == definitions.TYPE_PROFESSION:
        positive_item = common_train.get_positive_profession(person)
    else:
        raise TypeError

    return term == positive_item