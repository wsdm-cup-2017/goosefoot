import numpy as np
from sklearn import datasets, linear_model
import pickle
from definitions import LOGISTIC_MODEL_PATH



def load_model():
    return pickle.load(open(LOGISTIC_MODEL_PATH, 'rb'))


if __name__ == '__main__':
    loaded_model = load_model()
    # sample = np.array([1,2,3])
    # result = loaded_model.predict(sample)
