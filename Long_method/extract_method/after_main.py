# codecodecode

def modify_task(self, item):
    task_name = item.text()
    query_get_task_objects = '''SELECT task_object FROM taskbase WHERE task_name=\'{}\''''.format(task_name)
    task_tuple = sql_stuff.get_answer_as_teacher(query_get_task_objects)
    packed_task = task_tuple[0][0]
    task = pickle.loads(packed_task)
    edit_window = ModifyTaskForm(task)
    edit_window.exec()

# codecodecode
