from wsdm.ts.features import generalFeature
from wsdm.ts.features.tests import test_common

def test_has_file():
    print("----- HAS FILE -----")
    print("Expected to miss files:")
    for person in ["Alexandra Edenborough", "Anthony Aiello"]:
        print(person, generalFeature.has_file(person))

    print("\nExpected to have files:")
    for person in ["Zul Kifl Salami", "Zoya Krakhmalnikova", "Patrick Browne"]:
        print(person, generalFeature.has_file(person))

def test_positive():
    print("----- POSITIVE -----")
    print("\nExpected not to be positive nationalities:")
    for person, nationality in [("Arnold Schwarzenegger", "Austria"), ("Michael Jackson", "France"), ("Patrick Burns (businessman)", "Bulgaria")]:
        print(person, nationality, generalFeature.is_nationality_positive(person, nationality))

    print("\nExpected to be positive nationalities:")
    for person, nationality in [("Justus Hermann Lipsius", "Germany"), ("José Oquendo", "Puerto Rico"), ("Elka Nikolova", "Bulgaria")]:
        print(person, nationality, generalFeature.is_nationality_positive(person, nationality))

    print("\nExpected not to be positive professions:")
    for person, profession in [("Arnold Schwarzenegger", "Actor"), ("Michael Jackson", "Politician"), ("Patrick Burns (businessman)", "Violist")]:
        print(person, profession, generalFeature.is_profession_positive(person, profession))

    print("\nExpected to be positive professions:")
    for person, profession in [("Andrew Paul Leonard", "Photographer"), ("Koji Futada", "Politician"), ("Henryk Machalica", "Actor")]:
        print(person, profession, generalFeature.is_profession_positive(person, profession))


def test_negative():
    print("----- NEGATIVE -----")
    print("Expected not to be negative nationalities:")
    for person, nationality in [("Arnold Schwarzenegger", "Austria"), ("Michael Jackson", "France"), ("Patrick Burns (businessman)", "United States of America")]:
        print(person, nationality, generalFeature.is_nationality_negative(person, nationality))

    print("\nExpected to be negative nationalities:")
    for person, nationality in [("W. T. Tutte", "Kazakhstan"), ("Mara Brock Akil", "Algeria"), ("Ronnie Milsap", "Lithuania")]:
        print(person, nationality, generalFeature.is_nationality_negative(person, nationality))

    print("\nExpected not to be negative professions:")
    for person, profession in [("Arnold Schwarzenegger", "Actor"), ("Michael Jackson", "Dancer"), ("Maurice Prendergast", "Artist")]:
        print(person, profession, generalFeature.is_profession_negative(person, profession))

    print("\nExpected to be negative professions:")
    for person, profession in [("Stefan Hierländer", "Peace activist"), ("Olivér Halassy", "Philanthropist"), ("Maurice Prendergast", "Preacher")]:
        print(person, profession, generalFeature.is_profession_negative(person, profession))


def print_new_lines():
    print("\n\n")



if __name__ == '__main__':
    test_has_file()
    print_new_lines()
    test_positive()
    print_new_lines()
    test_negative()

