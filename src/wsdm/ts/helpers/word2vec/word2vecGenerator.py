import gensim, logging
import os
from src.wsdm.ts.helpers.persons import persons
from src.wsdm.ts.helpers.countries import countries

from definitions import WORD2VEC_MODEL_DIR
from definitions import PERSONS_DIR
from definitions import PROFESSIONS_DIR

from src.wsdm.ts.helpers.persons.common import split_to_words

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            file = open(os.path.join(self.dirname, fname), encoding='utf8')

            person_name = os.path.splitext(fname)[0]
            first_line = file.readline()
            alternative_names = persons.get_persons_names(first_line, person_name)
            # print(person_name,' -> ', alternative_names)
            file.seek(0)

            for line in file:
                line = countries.process_line(line)

                splitted = persons.process_splitted(split_to_words(line), person_name, alternative_names)

                yield [word.lower() for word in splitted]

model = gensim.models.Word2Vec(MySentences(PERSONS_DIR), workers=4, min_count=1)
model.train(MySentences(PROFESSIONS_DIR))

model.save(WORD2VEC_MODEL_DIR)
