def count_medium_day_temp_of_month(temp_array):
    """Сюда передается двумерный массив погоды за месяц
    вида [[date, start, end, high, low], ...]"""
    sum = 0
    for day in temp_array:
        day_sum = 0
        for i in day[1:]:
            day_sum += i
        sum += day_sum / 4
    return sum / len(temp_array)


def check_normal_weather(start, end, high, low):
    if (start == normal_start and
            end == normal_end and
            high == normal_high and
            low == normal_low):
        return True
    else:
        return False


def add_daily_measurement(temp_array, date, start, end, high, low):
    today_temps = list
    today_temps.append(date)
    today_temps.append(start)
    today_temps.append(end)
    today_temps.append(high)
    today_temps.append(low)

    temp_array.append(today_temps)
