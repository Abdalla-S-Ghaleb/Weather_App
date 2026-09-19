import requests
from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

key = os.getenv("API_KEY")

def get_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()
