import gensim
import logging
import traceback

from src.wsdm.ts.helpers.persons import persons
from src.wsdm.ts.helpers.countries import countries
from src.wsdm.ts.helpers.professions import professions

from definitions import WORD2VEC_MODEL_DIR

def load_module():
    global model
    model = gensim.models.Word2Vec.load(WORD2VEC_MODEL_DIR)

def find_profession_similarity(person_name, profession):
    global model

    person_name = persons.remove_spaces(person_name)
    profession_words = professions.get_similarity_words(profession)
    result = 0;
    for word in profession_words:
        try:
            result += model.similarity(person_name.lower(), word.lower())
        except Exception as e:
            logging.error(traceback.format_exc())
    result /= len(profession_words)
    return result

def find_nationality_similarity(person_name, nationality):
    global model

    person_name = persons.remove_spaces(person_name)
    nationality = countries.remove_spaces(nationality)
    try:
        return model.similarity(person_name.lower(), nationality.lower())
    except Exception as e:
        logging.error(traceback.format_exc())
        return 0