import numpy as np
from sklearn import linear_model
import pickle
import definitions
import os

from src.wsdm.ts.features import word2VecFeature
from src.wsdm.ts.helpers.logistic import logistic_utils

def get_data_and_labels(inputType):
    if inputType == definitions.TYPE_NATIONALITY:
        filename = os.path.join(definitions.TRAINING_DIR, "custom_nationality.train")
    elif inputType == definitions.TYPE_PROFESSION:
        filename = os.path.join(definitions.TRAINING_DIR, "custom_profession.train")

    data = []
    labels = []

    with open(filename, encoding='utf8', mode='r') as fr:
        for line in fr:
            splitted = line.rstrip().split('\t')
            assert len(splitted) == 3, "Invalid input row"
            person = splitted[0]
            term = splitted[1]
            score = splitted[2]

            data.append(logistic_utils.get_features_values(person, term, inputType, word2VecFeature))
            labels.append(score)

    return np.array(data), np.array(labels)


def train_and_save(inputType):
    if inputType == definitions.TYPE_NATIONALITY:
        filename = definitions.LOGISTIC_MODEL_NATIONALITY_PATH
    elif inputType == definitions.TYPE_PROFESSION:
        filename = definitions.LOGISTIC_MODEL_PROFESSION_PATH

    data, labels = get_data_and_labels(inputType)
    log_model = linear_model.LogisticRegression()
    log_model.fit(data, labels)
    pickle.dump(log_model, open(filename, 'wb'))

if __name__ == '__main__':
    word2VecFeature.load_module()

    train_and_save(definitions.TYPE_NATIONALITY)
    train_and_save(definitions.TYPE_PROFESSION)