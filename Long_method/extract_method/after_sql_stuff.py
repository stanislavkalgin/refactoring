import pymysql
from sql_links import *


def setup_connection_as_teacher():
    con = pymysql.connect(db_host, db_teacher_username,
                          db_teacher_password, db_database_name)
    cur = con.cursor()
    return con, cur


def get_answer_as_teacher(query):
    con, cur = setup_connection_as_teacher()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result