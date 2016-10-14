import gensim

from ..persons import persons
from ..countries import countries
from ..professions import professions

def load_module():
    global model
    model = gensim.models.Word2Vec.load('../../../../_DATA/word2vec_model.txt')

def find_profession_similarity(person_name, profession):
    global model

    person_name = persons.remove_spaces(person_name)
    profession_words = professions.get_similarity_words(profession)
    result = 0;
    for word in profession_words:
        result += model.similarity(person_name.lower(), word.lower())
    result /= len(profession_words)
    return result

def find_nationality_similarity(person_name, nationality):
    global model

    person_name = persons.remove_spaces(person_name)
    nationality = countries.remove_spaces(nationality)
    return model.similarity(person_name.lower(), nationality.lower())