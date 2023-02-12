# flake8: noqa

from tests.utils.standard_fixtures import (
    app,
    session_client,
    session_runner
)

from tests.namespaces.rates.fixtures import (
    session_get_average_price_with_correct_data,
    session_get_average_price_with_invalid_params_datatype,
    session_get_average_price_with_invalid_params_data
)
