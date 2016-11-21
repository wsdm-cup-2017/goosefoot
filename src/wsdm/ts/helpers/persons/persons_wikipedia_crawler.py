import os
import urllib.request
import urllib.parse
from wsdm.ts.helpers.persons import persons
import logging
import traceback
from definitions import PERSONS_DIR
from definitions import NOMENCLATURES_DIR
from multiprocessing.dummy import Pool as ThreadPool
from wsdm.ts.helpers.persons.common import get_html_content
from wsdm.ts.helpers.persons.common import modify_wikipedia_content


def download_file(*args):
    base_wiki_url = 'http://en.wikipedia.org/wiki/'
    # base_wiki_url = 'http://deletionpedia.org/en/'
    line = args[0]
    person_name = line.split('	', 1)[0]
    modified_name = persons.remove_spaces(person_name)
    file_name = os.path.join(PERSONS_DIR, modified_name + '.txt')
    url = base_wiki_url + urllib.parse.quote(person_name)

    wiki_file = None
    try:
        if not os.path.isfile(file_name):
            html_content = get_html_content(url)
            html_content = modify_wikipedia_content(html_content)

            wiki_file = open(file_name, encoding='utf8', mode='x')
            wiki_file.write(html_content)
    except urllib.error.HTTPError as e:
        print(str(e.code) + ": " + url)
    except Exception as e:
        logging.error(traceback.format_exc())
    finally:
        if wiki_file != None:
            wiki_file.close()

with open(os.path.join(NOMENCLATURES_DIR, 'missing_persons.txt'), encoding='utf8', mode='r') as f:
    pool = ThreadPool(4)
    pool.map(download_file, f)
