import requests


API_key = '3b2461f40913894931f208451ae8e549'

def get_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


# def load_icon(icon_code):
#     url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
#
#     response = requests.get(url)
#
#     if response.status_code != 200:
#         print("Failed to download icon:", response.status_code)
#         return None
#
#     return image.convert_alpha()