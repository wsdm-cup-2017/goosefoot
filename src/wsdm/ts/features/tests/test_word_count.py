
from src import definitions
from wsdm.ts.features import word_countFeature
from wsdm.ts.features.tests.test_common import calculate_similarities

if __name__ == '__main__':

    print("----- NATIONALITIES -----")
    calculate_similarities("wsdm_nationality.train", word_countFeature.find_similarity, definitions.TYPE_NATIONALITY)

    print("\n\n\n\n\n\n")
    print("----- PROFESSIONS -----")
    calculate_similarities("wsdm_profession.train", word_countFeature.find_similarity, definitions.TYPE_PROFESSION)