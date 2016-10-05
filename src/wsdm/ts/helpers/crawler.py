import urllib.request
import urllib.parse

def write_wikipedia_html_content(personName):
    url = 'http://en.wikipedia.org/wiki/' + urllib.parse.quote(personName)
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode("utf-8")

        try:
            htmlFile = open('../../../../_DATA/wikipedia/' + personName + '.html', encoding='utf8', mode='x')
            htmlFile.write(html_content)
            htmlFile.close()
            print(personName + ' added!')
        except FileExistsError as e:
            pass


f = open('../../../../_DATA/nomenclatures/persons.txt', encoding='utf8', mode='r')

for i, line in enumerate(f):
    name = line.split('	', 1)[0]
    write_wikipedia_html_content(name)
    if i > 20:
        break

f.close()
