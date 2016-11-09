from wsdm.ts.features import tfIdfFeature
from wsdm.ts.features.tests import test_common

if __name__ == '__main__':
    print("----- NATIONALITIES -----")
    # Nationalities
    test_common.calculate_similarities("wsdm_nationality.train", tfIdfFeature.find_nationality_similarity)

    print("----- PROFESSIONS -----")
    # Professions
    test_common.calculate_similarities("wsdm_profession.train", tfIdfFeature.find_profession_similarity)