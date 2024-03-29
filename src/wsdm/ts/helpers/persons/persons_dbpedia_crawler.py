import os
import urllib.request
import urllib.parse
from wsdm.ts.helpers.persons import persons
import logging
import traceback
from definitions import PERSONS_DIR
from definitions import NOMENCLATURES_DIR
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from wsdm.ts.helpers.persons.common import get_html_content

def modify_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    inner_content = soup\
        .find( "p", { "class" : "lead" })

    content_text = inner_content.get_text()

    # Remove empty lines:
    return os.linesep.join([s for s in content_text.splitlines() if s])

def download_file(*args):
    line = args[0]
    person_name = line.split('	', 1)[0]
    modified_name = persons.remove_spaces(person_name)
    file_name = os.path.join(PERSONS_DIR, modified_name + '.txt')
    url = 'http://dbpedia.org/page/' + urllib.parse.quote(modified_name)

    dbpedia_file = None
    try:
        if not os.path.isfile(file_name):
            html_content = get_html_content(url)
            html_content = modify_html_content(html_content)

            if len(html_content) > 0:
                dbpedia_file = open(file_name, encoding='utf8', mode='x')
                dbpedia_file.write(html_content)
    except urllib.error.HTTPError as e:
        print(str(e.code) + ": " + url)
    except Exception as e:
        logging.error(traceback.format_exc())
    finally:
        if dbpedia_file != None:
            dbpedia_file.close()

if __name__ == '__main__':
    with open(os.path.join(NOMENCLATURES_DIR, 'missing_persons.txt'), encoding='utf8', mode='r') as f:
        pool = ThreadPool(4)
        pool.map(download_file, f)
