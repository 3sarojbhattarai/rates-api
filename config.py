import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def get_database_info():

    database_info = {}
    database_info['host'] = os.getenv('DB_HOST')
    database_info['port'] = os.getenv('DB_PORT')
    database_info['username'] = os.getenv('DB_USERNAME')
    database_info['password'] = os.getenv('DB_PASSWORD')
    database_info['database'] = os.getenv('DB_NAME')
    return database_info


class Config:

    # ---------- Flask Related ------------

    # --------- Swagger Parameters ---------
    SWAGGER_TITLE = 'Rates API'
    SWAGGER_DESCRIPTION = 'API which calculates the average price of ocean and air freight rates'
    SWAGGER_VERSION = '1.0.0'

    # --------- Database Parameters ----------
    DATABASE_INFO = get_database_info()
