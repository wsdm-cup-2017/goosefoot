import gensim, logging
import countries

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __iter__(self):
        for line in open(self.file_name, encoding='utf8'):
            line = countries.process_line(line)
            yield line.split()

sentences = MySentences('../../../../_DATA/wikipedia/wiki-sentences.txt')
model = gensim.models.Word2Vec(sentences, workers=4)

model.save('../../../../_DATA/wikipedia/word2vec_model.txt')