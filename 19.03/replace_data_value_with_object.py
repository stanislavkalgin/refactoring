# before
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

# after
class User:
    def __init__(self, personal_name, login, password, rights='user'):
        self.id = Id()
        self.personal_name = personal_name
        self.login = login
        self.password = password
        self.rights = rights

class Id:
    def __init__(self):
        id_db = shelve.open(PATH_TO_USERS_DB, 'r')
        existing_ids = id_db.keys()
        while 1:
            new_id = int(str(randint(0, 10000)))
            if new_id not in existing_ids:
                break
        id_db.close()
        self.id = new_id

    def __str__(self):
        return self.id
