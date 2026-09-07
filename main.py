import pygame
import requests
from io import BytesIO

API_key = '3b2461f40913894931f208451ae8e549'


def initialize_screen():
    pygame.init()

    screen = pygame.display.set_mode((450, 500))
    pygame.display.set_caption("Weather App")

    return screen


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


def display(screen, weather, temp, icon):
    font = pygame.font.Font(None, 40)

    weather_text = font.render(weather, True, "black")
    temp_text = font.render(f"{temp:.1f}°C", True, "black")

    if icon is not None:
        screen.blit(icon, (170, 150))

    screen.blit(weather_text, (150, 270))
    screen.blit(temp_text, (180, 310))


def play(screen, input_box, button, font, city_name):
    active = False

    weather = None
    temp = None
    icon = None
    error = None

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:

                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if button.collidepoint(event.pos):

                    if city_name.strip():

                        data = get_data(city_name.strip())

                        if data is not None:

                            weather = data['weather'][0]['description']
                            temp = data['main']['temp'] - 273.15
                            icon_code = data['weather'][0]['icon']

                            icon = load_icon(icon_code)

                            error = None

                        else:
                            weather = None
                            temp = None
                            icon = None
                            error = "City not found"

            if event.type == pygame.KEYDOWN:

                if active:

                    if event.key == pygame.K_BACKSPACE:
                        city_name = city_name[:-1]

                    elif event.key == pygame.K_RETURN:
                        if city_name.strip():

                            data = get_data(city_name.strip())

                            if data is not None:

                                weather = data['weather'][0]['description']
                                temp = data['main']['temp'] - 273.15

                                icon_code = data['weather'][0]['icon']
                                icon = load_icon(icon_code)

                                error = None

                            else:
                                error = "City not found"

                    else:
                        city_name += event.unicode

        screen.fill("gray")

        pygame.draw.rect(screen, "lightgray", input_box)
        pygame.draw.rect(screen, "black", input_box, 2)

        text_surface = font.render(city_name, True, "black")
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        pygame.draw.rect(screen, "gray", button)

        button_text = font.render("Search", True, "white")
        screen.blit(button_text, (button.x + 15, button.y + 10))

        if weather is not None:
            display(screen, weather, temp, icon)

        if error is not None:
            error_text = font.render(error, True, "red")
            screen.blit(error_text, (170, 350))

        pygame.display.flip()


def main():
    screen = initialize_screen()

    input_box = pygame.Rect(80, 50, 250, 45)

    button = pygame.Rect(340, 50, 100, 45)

    font = pygame.font.Font(None, 32)

    city_name = ""

    play(screen, input_box, button, font, city_name)


if __name__ == '__main__':
    main()