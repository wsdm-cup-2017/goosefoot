import src.wsdm.ts.helpers.train.common_train as common_train


def is_nationality_positive(person, nationality):
    positive_nationality = common_train.get_positive_nationality(person)
    return nationality == positive_nationality


def is_profession_positive(person, profession):
    positive_profession = common_train.get_positive_profession(person)
    return profession == positive_profession