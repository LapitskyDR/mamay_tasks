from interface.db_api import Loader
import json
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import joblib
from pathlib import Path

MODEL = None
if Path('model.joblib').is_file():
    MODEL = joblib.load('model.joblib')


def predict(answers):
    """
    :param json answers:
    :return:
    :raise:
        400 - bad input
        401 - bad DB connexion
    """
    result = {}
    try:
        answers = np.array(json.loads(answers))
    except Exception as e:
        result['issues'] = 400
        return result
    loader = Loader()
    try:
        koefs = loader.get_table('Koefs')
    except Exception as e:
        result['issues'] = 401
        return result
    assert koefs.shape[0] == len(answers)
    res = koefs.apply(lambda x: x*answers)
    vector = res.sum()
    result['success'] = True
    result['vector'] = vector.to_json(orient='records')
    return result


def upload_table(upfile, table_name):
    if table_name == 'Коэффициенты':
        table_name = 'Koefs'
    elif table_name == 'Описание':
        table_name = 'Descriptions'
    else:
        raise KeyError(f'Undefined table {table_name}')
    loader = Loader()
    loader.post_tabel_by_xls(upfile, table_name)


def fit(upfile, out_name):
    data = pd.read_excel(upfile)
    print(data.columns)
    in_val = data.loc[:, data.columns != out_name].values
    out_val = data[out_name].values.reshape(-1, 1)
    model = DecisionTreeRegressor()
    model.fit(in_val, out_val)
    # bin_model = pickle.dumps(model)
    joblib.dump(model, './{}.joblib'.format('model'))
