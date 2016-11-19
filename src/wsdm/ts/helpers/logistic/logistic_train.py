import numpy as np
from sklearn import datasets, linear_model
import pickle
from definitions import LOGISTIC_MODEL_PATH

def train_and_save():
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target
    log_model = linear_model.LogisticRegression(C=1e5)
    log_model.fit(iris_X, iris_y)
    pickle.dump(log_model, open(LOGISTIC_MODEL_PATH, 'wb'))

if __name__ == '__main__':
    train_and_save()