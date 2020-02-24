class DayWeather:
    def __init__(self, date, start, end, high, low):
        self.date = date
        self.start = start
        self.end = end
        self.high = high
        self.low = low

    def get_day_medium(self):
        return (self.start + self.end + self.high + self.low) / 4

    def check_weather_is_normal(self):
        if (self.start == normal_start and
                self.end == normal_end and
                self.high == normal_high and
                self.low == normal_low):
            return True
        else:
            return False


def count_medium_day_temp_of_month(temp_array):
    sum = 0
    for day in temp_array:
        sum += day.get_day_medium()
    return sum / len(temp_array)



today_temps = DayWeather(date=get_current_date(),
                         start=get_today_start(),
                         end=get_today_end(),
                         high=get_today_high(),
                         low=get_today_low())

temp_array.append(today_temps)
