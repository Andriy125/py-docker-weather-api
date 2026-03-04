import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']

        print(f"Current weather in {city}: {temp}°C, {condition}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
