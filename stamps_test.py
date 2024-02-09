# question number 1
# logic fundamental
from datetime import datetime

import requests


def check_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# list version
def format_number_count(n):

    number_formatted_list = []

    for num in range(1, n + 1):
        if (check_prime_number(num)):
            continue
        elif (num % 3 == 0 and num % 5 == 0):
            number_formatted_list.append('FooBar')
        elif (num % 5 == 0):
            number_formatted_list.append('Bar')
        elif (num % 3 == 0):
            number_formatted_list.append('Foo')
        else:
            number_formatted_list.append(num)

    return list(reversed(number_formatted_list))


print(format_number_count(100))

# to string version, with comma on it


def format_number_count_to_string(n):

    number_formatted_list = []

    for num in range(1, n + 1):
        if (check_prime_number(num)):
            continue
        elif (num % 3 == 0 and num % 5 == 0):
            number_formatted_list.append('FooBar')
        elif (num % 5 == 0):
            number_formatted_list.append('Bar')
        elif (num % 3 == 0):
            number_formatted_list.append('Foo')
        else:
            number_formatted_list.append(num)

    return ', '.join([str(num) for num in list(reversed(number_formatted_list))])


print(format_number_count_to_string(100))


# question number 2
# API Call from openweathermap


def parse_date(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    formatted_date = date_obj.strftime('%a, %d %b %Y')

    return formatted_date


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return str(round(celsius, 2)) + '\u00b0C'


# get data from API
try:
    response = requests.get(
        url='https://api.openweathermap.org/data/2.5/forecast?q=Jakarta&APPID=22924f851edb8ba3c5921e8c1ae2d1a5')
    weather_data = response.json()
except:
    print('error')

# get forcasted weather
forecasted_weathers = weather_data['list']

# parsing all forcasted weather
parsed_forcasted_weather = [parse_date(str(obj['dt_txt'])) + ':' +
                            str(kelvin_to_celsius(obj['main']['temp'])) for obj in forecasted_weathers]

grouped_forcasted_weather = []

# grouping all temperature based on its date
for item in parsed_forcasted_weather:
    date_part, temp_part = item.split(':')

    # Check if the date already exists in the result list
    date_exists = False
    for entry in grouped_forcasted_weather:
        if entry['date'] == date_part:
            entry['temperature'].append(temp_part)
            date_exists = True
            break

    # If date does not exist, create a new entry
    if not date_exists:
        grouped_forcasted_weather.append(
            {'date': date_part, 'temperature': [temp_part]})

# print the first occured temperature on a day
forecast_result = 'Weather forecast:\n'

for entry in grouped_forcasted_weather:
    date = entry['date']
    temperature = entry['temperature'][0]
    forecast_result += date + ': ' + temperature + '\n'

print(forecast_result)
