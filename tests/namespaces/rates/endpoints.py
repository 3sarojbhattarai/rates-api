

def get_average_price(self, query_params):
    return self.get(
        '/rates/regions',
        query_string=(query_params)
    )
