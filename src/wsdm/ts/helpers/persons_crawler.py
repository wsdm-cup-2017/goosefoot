import os
import urllib.request
import urllib.parse
import persons
from time import gmtime, strftime
from bs4 import BeautifulSoup

def get_html_content(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

def modify_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    inner_content = soup\
        .find( "div", { "id" : "mw-content-text" })\
        .find_all(["h2", "p"])

    inner_content = BeautifulSoup('\n\n'.join(str(s) for s in inner_content), "html.parser")
    content_text = inner_content.get_text()

    # Remove empty lines:
    return os.linesep.join([s for s in content_text.splitlines() if s])

def download_file(i, line):
    person_name = line.split('	', 1)[0]
    modified_name = persons.remove_spaces(person_name)
    file_name = '../../../../_DATA/persons/' + modified_name + '.txt'
    url = 'http://en.wikipedia.org/wiki/' + urllib.parse.quote(person_name)

    wiki_file = None
    try:
        if not os.path.isfile(file_name):
            html_content = get_html_content(url)
            html_content = modify_html_content(html_content)

            wiki_file = open(file_name, encoding='utf8', mode='x')
            wiki_file.write(html_content)
    except urllib.error.HTTPError as e:
        print(str(e.code) + ": " + url)
    finally:
        if wiki_file != None:
            wiki_file.close()

    if (i + 1) % 100 == 0:
        print("------- " + str(i + 1) + " persons added: Now on " + person_name + " (" + strftime("%H:%M:%S", gmtime()) + ") -------")

with open('../../../../_DATA/nomenclatures/persons.txt', encoding='utf8', mode='r') as f:
    for i, line in enumerate(f):
        download_file(i, line)
