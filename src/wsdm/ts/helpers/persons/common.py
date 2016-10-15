import urllib
import os
from bs4 import BeautifulSoup
import re

header = {'User-Agent': 'Mozilla/5.0'}

def split_to_words(input):
    return re.findall(r"[\w']+", input)

def get_html_content(url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0')
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")

def modify_wikipedia_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    inner_content = soup\
        .find( "div", { "id" : "mw-content-text" })\
        .find_all(["h2", "p"])

    inner_content = BeautifulSoup('\n\n'.join(str(s) for s in inner_content), "html.parser")
    content_text = inner_content.get_text()

    # Remove empty lines:
    return os.linesep.join([s for s in content_text.splitlines() if s])
