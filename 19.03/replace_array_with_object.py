#before
personal_information_fields = ['name', 'age', 'gender', 'is married', 'job', 'income']
personal_information_values = ['Igor Katamaranov', 31, 'm', False, 'builder', 35000]

class BankAccount:
    def __init__(self, personal_info, acc_type, client_type, department):
        self.personal_information = personal_info
        self.acc_type = acc_type
        self.client_type = client_type
        self.department = department
        self.credit_limit = personal_info[5] * 6

    def should_be_closed(self):
        if self.personal_information[4] in prohibited_jobs:
            if self.personal_information[5] <= 50_000:
                return True
            else:
                return False
        else:
            return False

#after
class Person:
    def __init__(self, name, age, gender, is_married, job, income):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_married = is_married
        self.job = job
        self.income = income

class BankAccount:
    def __init__(self, person, acc_type, client_type, department):
        self.personal_information = person
        self.acc_type = acc_type
        self.client_type = client_type
        self.department = department
        self.credit_limit = person.income * 6

    def should_be_closed(self):
        if self.personal_information.job in prohibited_jobs:
            if self.personal_information.income <= 50_000:
                return True
            else:
                return False
        else:
            return False
