import pymysql
from .prod import ProdDatabase
from .staging import StagingDatabase
from .preprod import PreProdDatabase
from .local import LocalDatabase


class Database:
    def __init__(self):
        pass

    @staticmethod
    def connection(db_env):
        databases = {
            'prod': ProdDatabase,
            'staging': StagingDatabase,
            'preprod': PreProdDatabase,
            'local': LocalDatabase
        }
        selected_db = databases[db_env]
        connection = pymysql.connect(host=selected_db['endpoint'],
                                     port=3306,
                                     user=selected_db['username'],
                                     passwd=selected_db['password'],
                                     db=selected_db['database_name'])
        cursor = connection.cursor()
        return cursor
