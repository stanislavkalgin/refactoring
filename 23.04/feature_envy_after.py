class Phone:
    def __init__(self, unform_number):
        self.unf_number = unform_number

    def get_country_code(self):
        return self.unf_number[:2]

    def get_area_code(self):
        return self.unf_number[2:5]

    def get_number(self):
        return self.unf_number[5:]

    def get_formatted_phone_number(self):
        return (self.get_country_code() + "("
                + self.get_area_code() + ")"
                + self.get_number())


class Person:
    def __init__(self, data_1, data_2):
        self.data_1 = data_1
        self.data_2 = data_2
        self.phone = Phone("+79234568999")

    def get_mobile_phone_number(self):
        return self.phone.get_formatted_phone_number()


a = Person(1, 2)
print(a.get_mobile_phone_number())
