import os
from src.wsdm.ts.helpers.persons import persons
from definitions import NOMENCLATURES_DIR
from definitions import PERSONS_DIR

def init_countries_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "nationalities.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            country = line.rstrip()
            result[country] = []

    return result

def init_professions_dict():
    result = {}
    with open(os.path.join(NOMENCLATURES_DIR, "professions.txt"), encoding='utf8', mode='r') as fr:
        for line in fr:
            country = line.rstrip()
            result[country] = []

    return result

init_professions_dict()
