from flask_restx import Resource, reqparse

from app.api.rates.api import rates_api
from app.api.rates.dto import DefaultResponsesDTO, RatesResponseDTO
from app.api.rates.service import get_average_price

# Ports related Args
ports_args = reqparse.RequestParser()
ports_args.add_argument('origin', type=str, required=True, default='CNSGH', help='Origin Port/Region')
ports_args.add_argument('destination', type=str, required=True, default='north_europe_main', help='Destination Port/Region')

# Datetime Related Args
date_args = reqparse.RequestParser()
date_args.add_argument('date_from', type=str, required=True, default='2016-01-01', help='Date from')
date_args.add_argument('date_to', type=str, required=True, default='2016-01-10', help='Date to')


@rates_api.route('/regions')
class EndPointRegionAveragePrice(Resource):

    @rates_api.expect(ports_args, date_args)
    @rates_api.response(200, 'Success', RatesResponseDTO.get_rates_output)
    @rates_api.response(400, 'Input Validation Error', DefaultResponsesDTO.input_validation_error_model)
    @rates_api.response(500, 'Error', DefaultResponsesDTO.error_model)
    def get(self):
        """ Get average rate between two regions on a specified date range """

        # Getting all the args
        p_args = ports_args.parse_args()
        d_args = date_args.parse_args()

        return get_average_price(
            origin=p_args['origin'], destination=p_args['destination'], date_from=d_args['date_from'], date_to=d_args['date_to'])


@rates_api.route('/health')
class PingPong(Resource):

    @rates_api.expect()
    @rates_api.response(200, 'Success')
    def get(self):
        """ Check health"""

        return 'OK'
