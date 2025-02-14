import json
import pygame
#class Tileset(object):
    #def __init__(self,id = '1',name = 'Tiny Swords',description = 'Tileset made by Pixel Frog',tileSize = '64',):
    #    self.id = id
    #    self.name = name
    #    self.desscription = description
    #    self.tilesize = tileSize
def load_tileset(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data

class Tile(object):
    def __init__(self, **data):
        self.__dict__.update(data)

class Layer(object):
    def __init__(self, **data):
        self.tiles = [] # list
        for tile in data['tiles']:
            t = Tile(**tile)
            self.tiles.append(t)
        data.pop('tiles')
        self.__dict__.update(data)

import base64, io
from PIL import  Image
def strToImage(v):
    b = base64.b64decode(v[22:])
    bb = io.BytesIO(b)
    img = Image.open(bb)
    #img = Image.open(io.bytesIO(base64.b64decode(v[22:])))
    return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

class Tileset(object):
    def __init__(self,fname = 'Tiny_Swords.json'):
        data = load_tileset(fname)
        self.layers = [] # list

        for layer in data['layers']:
            #print(layer['id'], layer['name'])
            _layer = Layer(**layer)
            self.layers.append(_layer)
        self.spriteSheets = {}#data['spriteSheets']

        for k,v in data['spriteSheets'].items():
            self.spriteSheets[k] = strToImage(v)

        self.names = list(self.spriteSheets.keys())
        self.name_index = 0
        #self.__dict__.update(kwargs)
        data.pop('layers')
        data.pop('spriteSheets')
        self.__dict__.update(data)

    def show_spriteSheet_name(self, font, screen):
        name = self.names[self.name_index]
        text = font.render(name,True,30)
        screen.blit(text,(20,550))

    def show_fps(self, font, screen, clock):
        message = f'{clock.get_fps():.2f}FPS'
        text = font.render(message, True, 30)
        screen.blit(text, (800 - text.get_width(), 550))

    def draw(self,screen):
        name = self.names[self.name_index]
        screen.blit(self.spriteSheets[name],(10,20))

    def up(self):
        self.name_index = (self.name_index+1)%len(self.names)
    def down(self):
        self.name_index = (self.name_index-1) % len(self.names)


#t = Tileset()
#for layer in t.layers:
#    print(layer.id, layer.name)

from pygame.locals import *
from pygame.font import Font
pygame.init()
screen = pygame.display.set_mode((800,600))
#logo = pygame.image.load('map.json')
#pygame.display.set_icon(logo)
pygame.display.set_caption('Kaitong')
font = Font('R.ttf',14)
tileset = Tileset()
clock = pygame.time.Clock()
running = True

while running:
    # check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in [K_LEFT,K_DOWN]:
                tileset.down()
            elif event.key in [K_RIGHT,K_UP]:
                tileset.up()

    screen.fill((125, 125, 125))
    tileset.show_spriteSheet_name(font,screen)
    tileset.show_fps(font,screen,clock)
    tileset.draw(screen)
    clock.tick(120)
    pygame.display.flip()