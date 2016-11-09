from wsdm.ts.features import tfIdfFeature
from wsdm.ts.features.tests import test_common

if __name__ == '__main__':
    print("----- PROFESSIONS -----")
    # Professions
    test_common.calculate_similarities("wsdm_profession.train", tfIdfFeature.find_profession_similarity)