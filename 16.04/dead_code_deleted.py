class User:
    def __init__(self, personal_name, login, password, rights='user'):
        id_db = shelve.open(PATH_TO_USERS_DB, 'r')
        existing_ids = id_db.keys()
        while 1:
            new_id = str(randint(0, 10000))
            if new_id not in existing_ids:
                break
        id_db.close()
        self.id = new_id
        self.personal_name = personal_name
        self.login = login
        self.password = password
        self.rights = rights


# class ModifyTaskForm(QtWidgets.QDialog):
def set_default_figure_fields(self):
    self.logic_figure_to_delete_is_chosen = False
    self.edited_figure_number = None
    self.edited_figure_key_symbols = []
    self.edited_figure_possible_symbols = []
    self.edited_figure_type = None
    self.edited_figure_key_symbols_text = ''
    self.edited_figure_possible_symbols_text = ''

    self.ui.figure_info_key_words.setText(self.edited_figure_key_symbols_text)
    self.ui.figure_info_possible_words.setText(self.edited_figure_possible_symbols_text)
    self.ui.figure_info_type.setText('Тип оборота')
    

class TextWindow(QtWidgets.QDialog):
    def __init__(self, text):
        super().__init__()
        self.ui = Ui_text_window()
        self.ui.setupUi(self)
        self.ui.text.setText(text)
