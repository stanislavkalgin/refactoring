def check_login_password(self):
    login = self.ui.entrance_login.text()
    password = self.ui.entrance_password.text()

    query_login_student = 'SELECT * FROM users'
    students = sql_stuff.get_answer_as_student(query_login_student)

    for i in range(len(students)):
        if students[i][1] == login and students[i][2] == password:
            setup_window(students, i)
            break
        else:
            self.ui.entrance_label.setText('Неудача')  # todo более цивильный текст


def setup_window(self, students, i):
    self.user_id = students[i][0]
    self.user_name = students[i][3]
    self.ui.stackedWidget.setCurrentIndex(2)
    query_get_task_names = '''SELECT `task_name` FROM taskbase ORDER BY task_name'''
    tasks = sql_stuff.get_answer_as_student(query_get_task_names)
    for j in range(len(tasks)):
        self.ui.task_list.addItem(tasks[j][0])