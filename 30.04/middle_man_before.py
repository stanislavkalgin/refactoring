from datetime import datetime


class Interface(InterfaceLibrary):
    def __init__(self):
        super.__init__()

    def set_default_window_values(self):
        default_object = DefaultObject()
        self.ui.name_field.set_text(default_object.name)
        self.ui.date_field.set_text(default_object.date)
        self.ui.status_field.set_text(default_object.status)


class DefaultObject():
    def __init__(self):
        self.name = "John Doe"
        self.date = datetime.date(datetime.now())
        self.status = check_status(self.name)


def check_status(name):
    return get_status_from_db(name)

