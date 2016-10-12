import gensim, logging
import os
import countries

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname), encoding='utf8'):
                line = countries.process_line(line)
                yield line.lower().split()

persons_folder = MySentences('../../../../_DATA/persons')
professions_folder = MySentences('../../../../_DATA/professions')

wiki_sentences_folder = MySentences('../../../../_DATA/wiki_sentences')

model = gensim.models.Word2Vec(persons_folder, workers=4, min_count=1)
model.train(professions_folder)

model.save('../../../../_DATA/word2vec_model.txt')