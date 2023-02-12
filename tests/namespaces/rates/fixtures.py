
import pytest

from tests.namespaces.rates.endpoints import get_average_price
from tests.namespaces.rates.utils import (
    generate_correct_get_average_price_query_string_data,
    generate_random_get_average_price_query_string_data,
    generate_random_get_average_price_query_string_with_incorrect_data_type)


# TestGetAveragePrice Related fixtures
@pytest.fixture()
def session_get_average_price_with_correct_data(session_client):

    query_params = generate_correct_get_average_price_query_string_data()
    return get_average_price(self=session_client, query_params=query_params)


@pytest.fixture()
def session_get_average_price_with_invalid_params_datatype(session_client):

    query_params = generate_random_get_average_price_query_string_with_incorrect_data_type()
    return get_average_price(self=session_client, query_params=query_params)


@pytest.fixture()
def session_get_average_price_with_invalid_params_data(session_client):

    query_params = generate_random_get_average_price_query_string_data()
    return get_average_price(self=session_client, query_params=query_params)
