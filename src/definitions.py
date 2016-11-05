import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, os.pardir, "_DATA")
NOMENCLATURES_DIR = os.path.join(DATA_DIR, "nomenclatures")
PROFESSIONS_DIR = os.path.join(DATA_DIR, "professions")
TEST_DIR = os.path.join(DATA_DIR, "test_sets")
TRAINING_DIR = os.path.join(DATA_DIR, "training_sets")

BIG_DATA_DIR = 'D:/WSDM_BIG_DATA/'
PERSONS_DIR = os.path.join(BIG_DATA_DIR, "persons")
TFIDF_PROFESSIONS_DIR = os.path.join(BIG_DATA_DIR, "tfidf_professions")
WORD2VEC_MODEL_PATH = os.path.join(BIG_DATA_DIR, "word2vec/word2vec_model.txt")
