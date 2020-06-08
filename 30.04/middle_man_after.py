from datetime import datetime


class Interface(InterfaceLibrary):
    def __init__(self):
        super.__init__()

    def set_default_window_values(self):
        self.ui.name_field.set_text("John Doe")
        self.ui.date_field.set_text(datetime.date(datetime.now()))
        self.ui.status_field.set_text(check_status("John Doe"))


def check_status(name):
    return get_status_from_db(name)
