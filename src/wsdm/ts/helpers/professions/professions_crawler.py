import os
import urllib.request
import urllib.parse
from time import gmtime, strftime
from bs4 import BeautifulSoup
from definitions import NOMENCLATURES_DIR
from definitions import PROFESSIONS_DIR

def get_html_content(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

def modify_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    inner_content = soup\
        .find( "div", { "id" : "mw-content-text" })\
        .find_all(["h2", "p"])

    inner_content = BeautifulSoup('\n\n'.join(str(s) for s in inner_content), "html.parser")

    return inner_content.get_text()

f = open(os.path.join(NOMENCLATURES_DIR, 'professions.txt'), encoding='utf8', mode='r')

for i, line in enumerate(f):
    init_profession = line.rstrip()
    file_name = os.path.join(PROFESSIONS_DIR, init_profession + '.txt')
    file_name = file_name.replace('"', "_")

    profession = init_profession
    if profession == 'American football player':
        profession = 'American football'
    elif profession == 'Film Art Director':
        profession = 'Art Director'
    elif profession == 'Film Score Composer':
        profession = 'Film Score'
    elif profession == 'Game Show Host':
        profession = 'Game show host'
    elif profession == 'Ice hockey player':
        profession = 'Ice hockey'
    elif profession == 'Jazz Composer':
        profession = 'Jazz'
    elif profession == 'Military aviator':
        profession = 'Military aviation'
    elif profession == 'Rodeo performer':
        profession = 'Rodeo'
    elif profession == 'Scenic Designer':
        profession = 'Scenic Design'
    elif profession == 'Soccer Player':
        profession = 'Football player'
    elif profession == 'Sound Sculptor':
        profession = 'Sound sculpture'
    elif profession == 'Television Show Host':
        profession = 'Presenter'
    elif profession == 'TV Editor':
        profession = 'Television crew'

    url = 'http://en.wikipedia.org/wiki/' + urllib.parse.quote(profession)

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

    if (i+1) % 20 == 0:
        print("------- " + str(i+1) + " professions added: Now on " + init_profession + " (" + strftime("%H:%M:%S", gmtime()) + ") -------")

f.close()
