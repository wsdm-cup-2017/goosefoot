from src import definitions
from wsdm.ts.features import word2VecFeature
from wsdm.ts.features import logisticFeature
from wsdm.ts.features.tests.test_common import calculate_similarities

if __name__ == '__main__':
    word2VecFeature.load_module()
    logisticFeature.load_modules(word2VecFeature)

    print("----- NATIONALITIES -----")
    calculate_similarities("wsdm_nationality.train", logisticFeature.find_similarity, definitions.TYPE_NATIONALITY)

    print("\n\n\n\n\n\n")
    print("----- PROFESSIONS -----")
    calculate_similarities("wsdm_profession.train", logisticFeature.find_similarity, definitions.TYPE_PROFESSION)