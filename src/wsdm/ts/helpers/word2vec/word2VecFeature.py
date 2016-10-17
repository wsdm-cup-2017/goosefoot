import gensim
import logging
import traceback

from src.wsdm.ts.helpers.persons import persons
from src.wsdm.ts.helpers.countries import countries
from src.wsdm.ts.helpers.professions import professions

from definitions import WORD2VEC_MODEL_DIR

DEFAULT_SIMILARITY = 3.5;
NATIONALITY_MULTIPLIER = 5;
PROFESSION_MULTIPLIER = 3;

def custom_similarity(similarity, multiplier = 1):
    result = similarity * 7;
    result *= multiplier
    if result > 7:
        result = 7
    return result;

def load_module():
    global model
    model = gensim.models.Word2Vec.load(WORD2VEC_MODEL_DIR)

def find_profession_similarity(person_name, profession):
    global model

    person_name = persons.remove_spaces(person_name)
    profession_words = professions.get_similarity_words(profession)
    result = 0;
    total_count = 0;
    for word in profession_words:
        try:
            result += abs(model.similarity(person_name.lower(), word.lower()))
            total_count += 1
        except Exception as e:
            logging.error(traceback.format_exc())

    if total_count == 0:
        return DEFAULT_SIMILARITY

    result /= total_count
    return custom_similarity(result, PROFESSION_MULTIPLIER)

def find_nationality_similarity(person_name, nationality):
    global model

    person_name = persons.remove_spaces(person_name)
    nationality = countries.remove_spaces(nationality)
    try:
        return custom_similarity(abs(model.similarity(person_name.lower(), nationality.lower())), NATIONALITY_MULTIPLIER)
    except Exception as e:
        logging.error(traceback.format_exc())
        return DEFAULT_SIMILARITY