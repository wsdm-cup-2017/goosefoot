from src import definitions
from wsdm.ts.features import word2VecFeature
from wsdm.ts.features import regressionFeature
from wsdm.ts.features import word_countFeature
from wsdm.ts.features.tests.test_common import calculate_similarities

def find_similarity(person_name, term, inputType):
    return definitions.REGRESSION_MULTIPLIER * regressionFeature.find_similarity(person_name, term, inputType) \
        + definitions.WORD_COUNT_MULTIPLIER * word_countFeature.find_similarity(person_name, term, inputType)

if __name__ == '__main__':
    word2VecFeature.load_module()
    regressionFeature.load_modules(word2VecFeature)

    print("----- NATIONALITIES -----")
    calculate_similarities("wsdm_nationality.train", find_similarity, definitions.TYPE_NATIONALITY)

    print("\n\n\n\n\n\n")
    print("----- PROFESSIONS -----")
    calculate_similarities("wsdm_profession.train", find_similarity, definitions.TYPE_PROFESSION)

