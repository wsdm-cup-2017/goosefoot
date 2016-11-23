import numpy as np
from wsdm.ts.features import tfIdfFeature
from wsdm.ts.features import word_countFeature

def get_features_values(person_name, term, inputType, w2vecFeature):
    # TODO: Add more features
    return np.array([
        tfIdfFeature.find_similarity(person_name, term, inputType),
        w2vecFeature.find_similarity(person_name, term, inputType),
        word_countFeature.find_similarity(person_name, term, inputType)
    ])
