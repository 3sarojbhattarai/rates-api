"""
This files contains all the logic for the endpoints.
"""
from datetime import timedelta, datetime

from app.utils.dbutils import DBUtils
from app.utils.response import bad_request_response, success_response
from config import Config


def _get_all_ports(region):
    """
    Functions that gives all the ports of that region
    """

    __get_ports_count = f""" select * from ports p where code = '{region}' """

    _all_geographical_region = f"""
        select
            code
        from ports where parent_slug in (
            WITH RECURSIVE combined_region AS (
                select
                    slug
                FROM regions WHERE slug = '{region}'
                UNION
                    SELECT
                        r.slug
                        FROM regions r INNER JOIN combined_region s
                        ON r.parent_slug  = s.slug
            ) SELECT * FROM combined_region)
        """

    # Check if that region is port, if port return that port
    if len(region) == 5:
        with DBUtils(database_info=Config.DATABASE_INFO, autocommit=False) as db_conn:
            result = db_conn.execute_query(__get_ports_count)
        if len(result) == 1:
            return f"('{region}')"

    # Get all the ports of that geographical region
    with DBUtils(database_info=Config.DATABASE_INFO, autocommit=False) as db_conn:
        result = db_conn.execute_query(_all_geographical_region)
    result = tuple([row['code'] for row in result])

    return result


def get_average_price(origin, destination, date_from, date_to):

    # Find  all the ports in an origin region
    origin = _get_all_ports(origin)
    if not origin:
        return bad_request_response(reason='Origin region does not have any port')

    # Find all the ports in a destination region
    destination = _get_all_ports(destination)
    if not destination:
        return bad_request_response(reason='Destination region does not have any port')

    # Valdiate date_from and date_to and make datetime date object
    try:
        date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
        date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
    except ValueError:
        return bad_request_response(reason='date_from and date_to should be in YYYY-MM-DD format')

    # check if date from is greater than date to
    if date_from > date_to:
        return bad_request_response(reason='date_from should be less than date_to')

    # Query to get average prices of any two date ranges
    GET_AVERAGE_PRICE = f"""
        select
        day,
        case
            when COUNT(price)>3 THEN AVG(price)::int
            ELSE NULL
        end average_price
        from prices
        where
        day between '{date_from}' and '{date_to}'
        and orig_code in {origin}
        and  dest_code in {destination}
        group by day
        order by day
    """
    with DBUtils(database_info=Config.DATABASE_INFO, autocommit=False) as db_conn:
        result = db_conn.execute_query(GET_AVERAGE_PRICE)

    # Preprare a dictionary that maps day and its average price
    date_and_average_prices_relation = {}
    for row in result:
        date_and_average_prices_relation[row['day']] = row['average_price']

    # Ranges dates between date from and date to
    total_date_ranges = [date_from + timedelta(days=x) for x in range(((date_to - date_from).days) + 1)]

    # Preparing response on JSON format
    response_data = []
    for date in total_date_ranges:
        response_data.append({'day': date.strftime('%Y-%m-%d'), 'average_price': date_and_average_prices_relation.get(date)})

    return success_response(data=response_data)
