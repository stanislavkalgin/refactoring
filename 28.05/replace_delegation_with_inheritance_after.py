class CallsQueue:
    def __init__(self, numbers_list, city_code):
        self.queue = numbers_list[:]
        self.city_code = city_code
        self.refreshment_time = datetime.now()

    def get_next_number(self):
        return self.city_code + self.queue.pop(0)

    def add_number(self, number):
        self.queue.append(number)
        self.refreshment_time = datetime.now()


class AutomaticCallerQueue(CallsQueue):
    def __init__(self, numbers_list, city_code):
        super().__init__(numbers_list, city_code)
        self.session_start = datetime.now()
        self.session_expiration = datetime.now() + 28800
        self.operator = user.get_name()

    # code code code
    def get_next_call(self):
        return self.queue.get_next_number()

    def add_numbers_to_queue(self, numbers_list):
        for i in numbers_list:
            self.queue.add_number(i)
