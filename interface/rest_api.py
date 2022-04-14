from interface.db_api import Loader
import json
import numpy as np


def predict(answers):
    """
    :param json answers:
    :return:
    """
    answers = np.array(json.loads(answers))
    loader = Loader()
    koefs = loader.get_table('Koefs')
    assert koefs.shape[0] == len(answers)
    res = koefs.apply(lambda x: x*answers)
    vector = res.sum()
    return vector.to_json(orient='records')


def upload_table(upfile, table_name):
    if table_name == 'Коэффициенты':
        table_name = 'Koefs'
    elif table_name == 'Описание':
        table_name = 'Descriptions'
    else:
        raise KeyError(f'Undefined table {table_name}')
    loader = Loader()
    loader.post_tabel_by_xls(upfile, table_name)
