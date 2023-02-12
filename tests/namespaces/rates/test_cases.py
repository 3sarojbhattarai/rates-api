"""
    All the test cases are verify here.
"""


class TestGetAveragePrice:

    """
    URL: GET /rates/regions
    """

    def test_get_facilitity_with_correct_data(self, session_get_average_price_with_correct_data):
        """
        GIVEN - Prices between two regions in a specified date are on database
        WHEN - calls GET rates/regions with said origin and destination within date range
        WHAT - response.status_code == 200
        WHAT - RESPONSE data types should be their respective data type
        """

        # Check the response status code
        assert session_get_average_price_with_correct_data.status_code == 200

        # Check the data and its data type
        for row in session_get_average_price_with_correct_data.json:
            assert isinstance(session_get_average_price_with_correct_data.json['data'], list)

            assert isinstance(session_get_average_price_with_correct_data.json['data'][0]['day'], str)
            assert isinstance(session_get_average_price_with_correct_data.json['data'][0]['average_price'], (int, type(None)))

    def test_get_average_price_with_invalid_params_datatype(self, session_get_average_price_with_invalid_params_datatype):
        """
        GIVEN - Prices between two regions in a specified date are on database
        WHEN - calls GET rates/regions with random origin and destination region
        WHAT - response.status_code == 400
        """

        # Check the response status code
        assert session_get_average_price_with_invalid_params_datatype.status_code == 400

    def test_get_average_price_with_invalid_params_data(self, session_get_average_price_with_invalid_params_data):
        """
        GIVEN - Prices between two regions in a specified date are on database
        WHEN - calls GET rates/regions with random origin and destination region with incorrect data type
        WHAT - response.status_code == 400
        """

        # Check the response status code
        assert session_get_average_price_with_invalid_params_data.status_code == 400
