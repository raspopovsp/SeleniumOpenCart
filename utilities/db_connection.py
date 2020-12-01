from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()  # Костылим MySQL для Python3


def connect(req):
    engine = create_engine("mysql://root:root@localhost/opencartdb")
    result = engine.execute(req)

    res = result.fetchall()
    result.close()
    return res


def delete_row(req):
    engine = create_engine("mysql://root:root@localhost/opencartdb")
    result = engine.execute(req)
    result.close()


def insert_row(req):
    engine = create_engine("mysql://root:root@localhost/opencartdb")
    result = engine.execute(req)
    result.close()