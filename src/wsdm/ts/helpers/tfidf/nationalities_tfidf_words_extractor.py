import math
import re
import os
import time
from collections import Counter
from collections import defaultdict

from definitions import NOMENCLATURES_DIR, TFIDF_NATIONALITIES_DIR


def get_lower_words(text):
    return re.findall(r"\b[a-z]+\b", text)


def tf(word, nationality, words_dict, doc_words_count):
    return words_dict[word][nationality] / doc_words_count


def idf(word, total_count, words_dict):
    return math.log(total_count / (1 + len(words_dict[word])))


def tfidf(word, nationality, total_count, words_dict, doc_words_count):
    return tf(word, nationality, words_dict, doc_words_count) * idf(word, total_count, words_dict)


def get_nationalities_words_list():
    with open(os.path.join(NOMENCLATURES_DIR, 'nationalities.txt'), encoding='utf8', mode='r') as f:
        for line in f:
            nationality = line.rstrip()
            with open(os.path.join(TFIDF_NATIONALITIES_DIR, nationality + '.txt'), encoding='utf8', mode='r') as prof_file:
                yield nationality, get_lower_words(prof_file.read())


def get_nationalities_list():
    return [line.rstrip() for line in open(os.path.join(NOMENCLATURES_DIR, 'nationalities.txt'), encoding='utf8', mode='r')]


def init_words_dict():
    result = defaultdict(dict)
    index = 1
    for nationality, doc_words in get_nationalities_words_list():
        document_dict = Counter(doc_words)
        for word in document_dict:
            if len(result) % 20000 == 0:
                print(index, "document:", len(result), "words", time.strftime("%H:%M:%S"))
            result[word][nationality] = document_dict[word]
        index += 1

    return result


def main():
    nationalities = get_nationalities_list()
    words_dict = init_words_dict()

    print("{")
    for nationality, doc_words in get_nationalities_words_list():
        scores = {word: tfidf(word, nationality, len(nationalities), words_dict, len(doc_words)) for word in doc_words}

        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:20]
        print("# {0}".format(time.strftime("%H:%M:%S")))
        print("'{0}': {{".format(nationality))
        for word, score in sorted_words:
            print("\t'{0}': {1},".format(word, round(score, 8)))
        print('},')
    print("}")

if __name__ == '__main__':
    main()