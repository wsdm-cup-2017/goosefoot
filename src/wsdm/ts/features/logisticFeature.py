import definitions
import pickle
from src.wsdm.ts.helpers.logistic import logistic_utils
import numpy as np

nationality_model = None
profession_model = None
word2VecFeature = None

def load_modules(w2vFeature):
    global nationality_model
    global profession_model
    global word2VecFeature

    nationality_model =  pickle.load(open(definitions.LOGISTIC_MODEL_NATIONALITY_PATH, 'rb'))
    profession_model =  pickle.load(open(definitions.LOGISTIC_MODEL_PROFESSION_PATH, 'rb'))
    word2VecFeature = w2vFeature


def find_similarity(person_name, term, inputType):
    global nationality_model
    global profession_model
    global word2VecFeature

    data = logistic_utils.get_features_values(person_name, term, inputType, word2VecFeature)
    data = data.reshape(1,-1)

    if inputType == definitions.TYPE_NATIONALITY:
        score =  nationality_model.predict(data)
    elif inputType == definitions.TYPE_PROFESSION:
        score = profession_model.predict(data)
    else:
        raise TypeError

    assert len(score) == 1
    result = float(score[0])
    if result > 7:
        result = 7
    if result < 0:
        result = 0
    return result

