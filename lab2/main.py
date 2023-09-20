import requests
from dotenv import dotenv_values

config = dotenv_values("settings.env")

city_n = 0
city = ""
api_key = config['API_KEY']


def get_weather(city: str, api_key: str) -> dict:
    res = requests.request("get", "https://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'units': "metric", 'lang': "ru", 'appid': api_key})
    return res.json()


print("""1 - Москва
2 - Владивосток
3 - Лондон
4 - Киев
""")

try:
    city_n = int(input("Введите цифру какой город вы хотите выбрать >> ")) - 1
except ValueError:
    print("Только цифру....")
    city_n = 0
    print("Выбран город по умолчанию)")

match city_n:
    case 0:
        city = "Москва, Ru"
    case 1:
        city = "Владивосток, Ru"
    case 2:
        city = "Лондон, Uk"
    case 3:
        city = "Киев, Ua"
    case _:
        raise ValueError("Unknown city.")

data = get_weather(city, api_key)

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
