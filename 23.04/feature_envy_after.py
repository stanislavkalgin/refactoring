class Address:
    def __init__(self, city_name, street, house):
        self.city_name = city_name
        self.street = street
        self.house = house

    def get_city_code(self):
        global cities
        return cities[self.city_name]

    def get_city(self):
        return self.city_name

    def get_street_name(self):
        return self.street

    def get_house_number(self):
        return str(self.house)

    def get_str_address(self):
        return (self.get_city_code() + " " +
                self.get_city() + " "
                + self.get_street_name() + ", "
                + str(self.get_house_number()))


class Person:
    def __init__(self, data_1, data_2):
        self.data_1 = data_1
        self.data_2 = data_2
        self.address = Address("Moscow", "Lenin", 13)

    def get_full_address(self):
        return self.address.get_str_address()
