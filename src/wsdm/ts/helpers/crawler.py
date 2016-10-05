f = open('../../../../_DATA/nomenclatures/persons.txt', encoding='utf8', mode='r')

for i, line in enumerate(f):
    name = line.split('	', 1 )[0]
    print(name)