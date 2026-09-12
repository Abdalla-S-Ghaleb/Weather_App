from Weather import *


def main():
    screen = initialize_screen()

    input_box = pygame.Rect(80, 50, 250, 45)

    button = pygame.Rect(340, 50, 100, 45)

    font = pygame.font.Font(None, 32)

    city_name = ""

    play(screen, input_box, button, font, city_name)


if __name__ == '__main__':
    main()