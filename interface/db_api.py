import os
import pandas as pd
import io
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Loader:
    def __init__(self,):
        self.connexion_str = self._get_connexion_str()

    @staticmethod
    def _get_connexion_str():
        credentials = {
            'user': os.environ['DB_LOGIN'],
            'password': os.environ['DB_PASSWORD'],
            'host': os.environ['DB_HOST'],
            'dbname': os.environ['DB_NAME']
        }
        user, password, host, dbname = credentials['user'], credentials['password'], credentials['host'], credentials[
            'dbname']
        connexion_str = f'postgresql+psycopg2://{user}:{password}@{host}/{dbname}'
        return connexion_str

    def post_tabel_by_xls(self, upfile, table_name, method='replace'):
        data = pd.read_excel(upfile)
        data.to_sql(table_name, con=self.connexion_str, if_exists=method, index=False)

    def get_table(self, table_name):
        table = pd.read_sql_table(table_name, self.connexion_str,)
        table.set_index(table.columns[0], inplace=True)
        return table
