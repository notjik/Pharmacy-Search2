import requests
import pygame
from io import BytesIO
from PIL import Image


def get_img(coords, scoords):
    delta = '0.002'
    map_server = 'https://static-maps.yandex.ru/1.x/'
    params = {'spn': ','.join([delta, delta]),
              'l': 'map',
              'pt': f"{','.join(coords)},org~{','.join(scoords)},home",
              'pl': f"{','.join(coords)},{','.join(scoords)}"}
    response = requests.get(map_server, params=params)
    Image.open(BytesIO(response.content)).save('map.png')
    return 'map.png'


def show_map(mapp, rast, ul, name, rab):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(name, True,
                      (180, 0, 0))
    f2 = pygame.font.Font(None, 36)
    text2 = f2.render(ul, True,
                      (180, 0, 0))
    f3 = pygame.font.Font(None, 36)
    text3 = f3.render(rab, True,
                      (180, 0, 0))
    f4 = pygame.font.Font(None, 36)
    text4 = f4.render(f'{rast} м', True,
                      (180, 0, 0))
    screen.blit(pygame.image.load(mapp), (0, 0))
    screen.blit(text1, (0, 0))
    screen.blit(text2, (0, 30))
    screen.blit(text3, (0, 60))
    screen.blit(text4, (0, 90))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
