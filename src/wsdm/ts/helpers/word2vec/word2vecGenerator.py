import gensim, logging
import os
from ..persons import persons
from ..countries import countries

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
            file.seek(0)

            for line in file:
                line = countries.process_line(line)

                splitted = persons.process_splitted(line.split(), person_name, alternative_names)

                yield [word.lower() for word in splitted]

persons_folder = MySentences('../../../../_DATA/persons')
professions_folder = MySentences('../../../../_DATA/professions')

wiki_sentences_folder = MySentences('../../../../_DATA/wiki_sentences')

model = gensim.models.Word2Vec(persons_folder, workers=4, min_count=1)
model.train(professions_folder)

model.save('../../../../_DATA/word2vec_model.txt')