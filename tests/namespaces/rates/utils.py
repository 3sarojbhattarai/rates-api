"""
    Utils related to
"""

from faker import Faker

fake = Faker()


def generate_correct_get_average_price_query_string_data():

    # some correct value that are taken from database
    origin = 'CNSGH'
    destination = 'north_europe_main'
    date_from = '2016-01-01'
    date_to = '2016-01-10'

    return {'origin': origin, 'destination': destination, 'date_from': date_from, 'date_to': date_to}


def generate_random_get_average_price_query_string_data():

    origin = fake.word()
    destination = fake.word()
    date_from = fake.word()
    date_to = fake.word()

    return {'origin': origin, 'destination': destination, 'date_from': date_from, 'date_to': date_to}


def generate_random_get_average_price_query_string_with_incorrect_data_type():

    origin = fake.random_int()
    destination = fake.random_int()
    date_from = fake.random_int()
    date_to = fake.random_int()

    return {'origin': origin, 'destination': destination, 'date_from': date_from, 'date_to': date_to}
