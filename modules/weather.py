import requests

API_KEY = "1ef1f30d92a7b95ea8e547c171a1998b"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] == 200:

        temp = data["main"]["temp"]

        desc = data["weather"][0]["description"]

        return f"The temperature in {city} is {temp} degree Celsius with {desc}"

    return "Unable to fetch weather"