import re

def get_similarity_words(profession):
    return re.findall(r"[\w]+", profession)

