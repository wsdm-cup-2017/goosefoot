import urllib.request
import urllib.parse

def get_wikipedia_html_content(personName):
    url = 'http://en.wikipedia.org/wiki/' + urllib.parse.quote(personName)
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

def write_content_to_file(content, person_name):
        try:
            file = open('../../../../_DATA/wikipedia/' + person_name + '.txt', encoding='utf8', mode='x')
            file.write(content)
            file.close()
            print(person_name + ' added!')
        except FileExistsError as e:
            pass


f = open('../../../../_DATA/nomenclatures/persons.txt', encoding='utf8', mode='r')

for i, line in enumerate(f):
    person_name = line.split('	', 1)[0]
    html_content = get_wikipedia_html_content(person_name)
    write_content_to_file(html_content, person_name)
    if i > 30:
        break

f.close()
