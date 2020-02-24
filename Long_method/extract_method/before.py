def modify_task(self, item):
    task_name = item.text()
    query_get_task_objects = '''SELECT task_object FROM taskbase WHERE task_name=\'{}\''''.format(task_name)

    con = pymysql.connect(db_host, db_teacher_username,
                          db_teacher_password, db_database_name)
    cur = con.cursor()

    cur.execute(query)
    task_tuple = cur.fetchall()
    cur.close()
    con.close()
    packed_task = task_tuple[0][0]
    task = pickle.loads(packed_task)
    edit_window = ModifyTaskForm(task)
    edit_window.exec()
