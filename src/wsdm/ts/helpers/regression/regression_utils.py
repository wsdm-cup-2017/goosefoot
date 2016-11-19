import numpy as np
from src.wsdm.ts.features import tfIdfFeature

def get_features_values(person_name, term, inputType, w2vecFeature):
    # TODO: Add more features
    return np.array([
        tfIdfFeature.find_similarity(person_name, term, inputType),
        w2vecFeature.find_similarity(person_name, term, inputType)
    ])
