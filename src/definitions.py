import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, os.pardir, "_DATA")
NOMENCLATURES_DIR = os.path.join(DATA_DIR, "nomenclatures")
PROFESSIONS_DIR = os.path.join(DATA_DIR, "professions")
TEST_DIR = os.path.join(DATA_DIR, "test_sets")
TRAINING_DIR = os.path.join(DATA_DIR, "training_sets")

BIG_DATA_DIR = os.path.join(ROOT_DIR, os.pardir, os.pardir, "WSDM_BIG_DATA")
PERSONS_DIR = os.path.join(BIG_DATA_DIR, "persons")
TFIDF_PROFESSIONS_DIR = os.path.join(BIG_DATA_DIR, "tfidf_professions")
TFIDF_NATIONALITIES_DIR = os.path.join(BIG_DATA_DIR, "tfidf_nationalities")
WORD2VEC_MODEL_PATH = os.path.join(BIG_DATA_DIR, "word2vec/word2vec_model.txt")
LOGISTIC_MODEL_NATIONALITY_PATH = os.path.join(DATA_DIR, "logistic", "logistic_nationality_model.txt")
LOGISTIC_MODEL_PROFESSION_PATH = os.path.join(DATA_DIR, "logistic", "logistic_profession_model.txt")

TYPE_NATIONALITY = 'NATIONALITY'
TYPE_PROFESSION = 'PROFESSION'

DEFAULT_SIMILARITY = 3
MAX_SIMILARITY = 7
MIN_SIMILARITY = 0
