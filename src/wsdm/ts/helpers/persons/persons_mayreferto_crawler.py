import os
import urllib.request
import urllib.parse
from wsdm.ts.helpers.persons import persons
import logging
import traceback
from definitions import PERSONS_DIR
from definitions import NOMENCLATURES_DIR
from bs4 import BeautifulSoup
from wsdm.ts.helpers.persons.common import get_html_content
from wsdm.ts.helpers.persons.common import modify_wikipedia_content
from multiprocessing.dummy import Pool as ThreadPool

def get_alternative_urls(main_url):
    html_content =get_html_content(main_url)
    soup = BeautifulSoup(html_content, "html.parser")
    inner_content = soup \
        .find("div", {"id": "mw-content-text"}) \
        .find("ul") \
        .find_all("a")

    wikipedia_url = 'https://en.wikipedia.org'
    result = tuple(s['href'] if s['href'].startswith(wikipedia_url) else wikipedia_url + s['href'] for s in inner_content)
    return result

def download_file(person_name, file_name):
    main_url = 'http://en.wikipedia.org/wiki/' + urllib.parse.quote(person_name)
    urls = get_alternative_urls(main_url)

    wiki_file = None
    try:
        if not os.path.isfile(file_name):
            wiki_file = open(file_name, encoding='utf8', mode='x')

            for url in urls:
                try:
                    html_content = get_html_content(url)
                    html_content = modify_wikipedia_content(html_content)
                    wiki_file.write(html_content + "\n")
                except urllib.error.HTTPError as e:
                    print(str(e.code) + ": " + url)

    except Exception as e:
        logging.error(traceback.format_exc())
    finally:
        if wiki_file != None:
            wiki_file.close()

def handle_mayreferto_person(*args):
    line = args[0]
    person_name = line.split('	', 1)[0]
    modified_name = persons.remove_spaces(person_name)
    file_name = os.path.join(PERSONS_DIR, modified_name + '.txt')
    if os.path.isfile(file_name) and os.path.getsize(file_name) < 200:
        with open(file_name, encoding='utf8', mode='r') as person_file:
            first_line = person_file.readline()
            if 'may refer to' in first_line\
                    or 'is the name of' in first_line:
                person_file.close()
                os.remove(person_file.name)
                download_file(person_name, file_name)
                print(person_name)


if __name__ == '__main__':
    with open(os.path.join(NOMENCLATURES_DIR, "persons.txt"), encoding='utf8', mode='r') as fr:
        pool = ThreadPool(4)
        pool.map(handle_mayreferto_person, fr)
