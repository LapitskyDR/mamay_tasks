from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import os

import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def create_db():
    credentials = {
        'user': os.environ['DB_LOGIN'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'dbname': os.environ['DB_NAME']
    }
    user, password, host, dbname = credentials['user'], credentials['password'], credentials['host'], credentials[
        'dbname']
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{dbname}')

    base = declarative_base()

    class Koefs(base):
        __tablename__ = 'Koefs'
        __tableargs__ = {'comment': 'Коэффициенты ответов для рассчёта профиля disc'}
        id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
        d_score = Column(Float, comment='d фактор')
        i_score = Column(Float, comment='i фактор')
        s_score = Column(Float, comment='s фактор')
        c_score = Column(Float, comment='c фактор')


    class Descriptions(base):
        __tablename__ = 'Descriptions'
        __tableargs__ = {'comment': 'Описание профиля по вектору disc'}
        id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
        description = Column(String, comment='описание')

    base.metadata.drop_all(engine, )
    base.metadata.create_all(engine)
    engine.connect().close()
