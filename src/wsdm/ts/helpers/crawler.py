import os
import urllib.request
import urllib.parse
from time import gmtime, strftime
from bs4 import BeautifulSoup

def get_wikipedia_html_content(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

def modify_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    inner_content = soup\
        .find( "div", { "id" : "mw-content-text" })\
        .find_all(["h2", "p"])

    inner_content = BeautifulSoup('\n\n'.join(str(s) for s in inner_content), "html.parser")

    return inner_content.get_text()

def write_content_to_file(content, person_name):
        try:
            file = open('../../../../_DATA/wikipedia/crawl/' + person_name + '.txt', encoding='utf8', mode='x')
            file.write(content)
            file.close()
            print(person_name + ' added!')
        except FileExistsError as e:
            pass

f = open('../../../../_DATA/nomenclatures/persons.txt', encoding='utf8', mode='r')

for i, line in enumerate(f):
    person_name = line.split('	', 1)[0]
    file_name = '../../../../_DATA/wikipedia/' + person_name + '.txt'
    file_name = file_name.replace('"', "_")
    url = 'http://en.wikipedia.org/wiki/' + urllib.parse.quote(person_name)

    wiki_file = None
    try:
        if not os.path.isfile(file_name):
            html_content = get_wikipedia_html_content(url)
            html_content = modify_html_content(html_content)

            wiki_file = open(file_name, encoding='utf8', mode='x')
            wiki_file.write(html_content)
    except urllib.error.HTTPError as e:
        print(str(e.code) + ": " + url)
    finally:
        if wiki_file != None:
            wiki_file.close()

    if (i+1) % 50 == 0:
        print("------- " + str(i+1) + " persons added: Now on " + person_name + " (" + strftime("%H:%M:%S", gmtime()) + ") -------")

f.close()
