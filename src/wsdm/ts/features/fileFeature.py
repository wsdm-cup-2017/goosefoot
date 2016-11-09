import os
import definitions
import src.wsdm.ts.helpers.persons.persons as p_lib

def has_file(person):
    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
    return os.path.isfile(person_file)