"""
This files provides the input payload and output responses DTOs of rates namespaces.
"""

from flask_restx import fields

from app.api.rates.api import rates_api
from app.utils.dto import success_model, input_validation_error_model, error_model


class DefaultResponsesDTO:

    input_validation_error_model = input_validation_error_model(rates_api)
    error_model = error_model(rates_api)


class RatesResponseDTO:

    get_rates_output_model = rates_api.model(
        'get_rates_output',
        {
            'day': fields.String,
            'average_price': fields.String
        }
    )
    get_rates_output = success_model(rates_api, data_model=get_rates_output_model, is_list=True)
