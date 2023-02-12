import psycopg2


class DBUtils:

    def __init__(self, database_info, autocommit=False):

        self.__db_host = database_info['host']
        self.__db_port = database_info['port']
        self.__db_user = database_info['username']
        self.__db_pword = database_info['password']
        self.__db_database = database_info['database']
        self.__autocommit = autocommit

    def __enter__(self):

        self.__connection = psycopg2.connect(
            host=self.__db_host,
            port=self.__db_port,
            user=self.__db_user,
            password=self.__db_pword,
            dbname=self.__db_database)
        self.__connection.autocommit = self.__autocommit
        self.__cursor = self.__connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if not self.__autocommit:
            self.__connection.commit()

        if self.__cursor.closed is False:
            self.__cursor.close()

        self.__connection.close()

    def execute_query(self, query, data=None):
        self.__cursor.execute(query, data)
        columns = self.__cursor.description
        return [{columns[index][0]:column for index, column in enumerate(value)} for value in self.__cursor.fetchall()]
