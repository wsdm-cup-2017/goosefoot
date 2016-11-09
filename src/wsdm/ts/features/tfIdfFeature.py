import src.wsdm.ts.helpers.persons.persons as p_lib
from src.wsdm.ts.helpers.tfidf.professions_tfidf_dictionary import PROFESSIONS_DICT
from src.wsdm.ts.helpers.tfidf.nationalities_tfidf_dictionary import NATIONALITIES_DICT
import os
import definitions
from collections import Counter
import operator
import re


def split_into_sentences(text):
    caps = "([A-Z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"

    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def custom_similarity(person, key, words_dict):
    result = 0

    person_file = os.path.join(definitions.PERSONS_DIR, p_lib.remove_spaces(person) + ".txt")
    if os.path.isfile(person_file):
        with open(person_file, 'r', encoding='utf8') as fr:
            tfidf_words = words_dict[key]
            sorted_tfidf_words = sorted(tfidf_words.items(), key=operator.itemgetter(1))
            max_weight = sorted_tfidf_words[-1][1]

            file_content = fr.read()
            person_words = p_lib.split_to_words(file_content.lower())
            document_dict = Counter(person_words)
            sentences_count = len(split_into_sentences(file_content))

            for word in tfidf_words:
                current_word_weight = tfidf_words[word] / max_weight
                if word in document_dict:
                    result += document_dict[word] * current_word_weight

            result = result / sentences_count

    result *= 55

    if result > 7:
        return 7

    return result


def find_profession_similarity(person_name, profession):
    return custom_similarity(person_name, profession, PROFESSIONS_DICT)


# def find_nationality_similarity(person_name, nationality):
#     return custom_similarity(person_name, nationality, NATIONALITIES_DICT)
