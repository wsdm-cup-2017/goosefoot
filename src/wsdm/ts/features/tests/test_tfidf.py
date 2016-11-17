import definitions
from wsdm.ts.features import tfIdfFeature
from wsdm.ts.features.tests import test_common

if __name__ == '__main__':
    print("----- NATIONALITIES -----")
    test_common.calculate_similarities("wsdm_nationality.train", tfIdfFeature.find_similarity, definitions.TYPE_NATIONALITY)

    print("\n\n\n\n\n\n")
    print("----- PROFESSIONS -----")
    test_common.calculate_similarities("wsdm_profession.train", tfIdfFeature.find_similarity, definitions.TYPE_PROFESSION)
