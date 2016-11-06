import math
import re
import os
import time
from collections import Counter
from collections import defaultdict

from definitions import NOMENCLATURES_DIR, TFIDF_PROFESSIONS_DIR


def get_lower_words(text):
    return re.findall(r"\b[a-z]+\b", text)


def tf(word, words):
    return words.count(word) / len(words)


def idf(word, total_count, words_dict):
    return math.log(total_count / (1 + words_dict[word]))


def tfidf(word, doc_words, total_count, words_dict):
    return tf(word, doc_words) * idf(word, total_count, words_dict)


def get_professions_words_list():
    with open(os.path.join(NOMENCLATURES_DIR, 'professions.txt'), encoding='utf8', mode='r') as f:
        for line in f:
            profession = line.rstrip()
            with open(os.path.join(TFIDF_PROFESSIONS_DIR, profession + '.txt'), encoding='utf8', mode='r') as prof_file:
                yield get_lower_words(prof_file.read())


def get_professions_list():
    return [line.rstrip() for line in open(os.path.join(NOMENCLATURES_DIR, 'professions.txt'), encoding='utf8', mode='r')]


def init_words_dict():
    result = defaultdict(int)
    index = 1
    for doc_words in get_professions_words_list():
        document_dict = Counter(doc_words)
        for word in document_dict:
            if len(result) % 20000 == 0:
                print(index, "document:", len(result), "words", time.strftime("%H:%M:%S"))
            # result[word] += document_dict[word]
            result[word] += 1
        index += 1

    return result


def main():
    professions = get_professions_list()
    words_dict = init_words_dict()

    index = 0
    print("{")
    for doc_words in get_professions_words_list():
        scores = {word: tfidf(word, doc_words, len(professions), words_dict) for word in doc_words}

        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:20]
        print("'{0}': {{".format(professions[index]))
        for word, score in sorted_words:
            print("\t'{0}': {1},".format(word, round(score, 8)))
        print('}')
        index += 1
    print("}")

if __name__ == '__main__':
    main()