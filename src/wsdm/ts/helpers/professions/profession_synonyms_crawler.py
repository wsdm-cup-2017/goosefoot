import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

'''
    Returns the most relevant synonyms of the specified
    in the URL word. The function crawls the website
    http://www.thesaurus.com/

    Correct example for URL input parameter is:
    http://www.thesaurus.com/browse/artisan

    The function will not return the full synonym list,
    but only the most relevant words.

    In the context of WSDM 2017 triple scoring task,
    this function is used to provide similar professions.

    All synonyms will be returned as a semi-colon separated
    list.
'''
def get_synonyms_by_url(url):
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode("utf-8")
        soup = BeautifulSoup(html_content, "html.parser")

        result=''
        inner_content = soup.find('div', class_='relevancy-list')
        for link in inner_content:
            if ('#fcbb45' in str(link) or '#fbd48e' in str(link)):
                relevant_links = link.findAll('span', class_='text')
                for relevant_link in relevant_links:
                    relevant_link_str = str(relevant_link.contents)
                    result+=relevant_link_str
        return result.replace('\'][\'',';').replace('[','').replace(']','')

def main(argv):
    from wsdm.ts.helpers.professions import professions
    for profession in professions.all_professions_list:
        try:
            #uncomment the next line to retrieve all professions synonyms
            #synonyms = get_synonyms_by_url('http://www.thesaurus.com/browse/' + profession + '?s=t').lower()
            if (synonyms == ''):
                synonyms = ' '
            print('\'' + profession + '\'' + ':' + synonyms + ',')
        except:
            print('\'' + profession + '\'' + ':' + '\' \',')

if __name__ == '__main__':
    main([])

