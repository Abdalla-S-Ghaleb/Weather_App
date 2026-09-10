import requests
from io import BytesIO
import pygame


def get_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def load_icon(icon_code):
    url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to download icon:", response.status_code)
        return None

    image = pygame.image.load(BytesIO(response.content))
    return image.convert_alpha()