class AutomaticCallerQueue:
    def __init__(self):
        self.session_start = datetime.now()
        self.session_expiration = datetime.now() + 28800
        self.operator = user.get_name()
        self.call_queue = CallsQueue(session.get_phone_numbers())

    # code code code
    def get_next_call(self):
        return self.call_queue.get_next_number()

    def add_numbers_to_queue(self, numbers_list):
        for i in numbers_list:
            self.call_queue.add_number(i)


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
