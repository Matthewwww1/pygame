import json
import pygame
import base64
import io
from PIL import Image
from pygame.locals import *
from pygame.font import Font

# Load tileset data from JSON
def load_tileset(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data

# Convert base64 image string to a Pygame image
def strToImage(v):
    b = base64.b64decode(v[22:])  # Assuming base64 is formatted correctly
    bb = io.BytesIO(b)
    img = Image.open(bb)  # Corrected to use Image.open instead of Image
    img = img.convert("RGBA")  # Ensure it's in RGBA mode
    return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

# Define the Tile class
class Tile(object):
    def __init__(self, **data):
        self.__dict__.update(data)

# Define the Layer class to hold tiles
class Layer(object):
    def __init__(self, **data):
        self.tiles = []  # list of tile objects
        for tile in data['tiles']:
            t = Tile(**tile)
            self.tiles.append(t)
        data.pop('tiles')  # Remove the tiles key as it's already processed
        self.__dict__.update(data)

# Define the Tileset class to handle tileset and sprite sheet
class Tileset(object):
    def __init__(self, fname='Tiny_Swords.json'):
        data = load_tileset(fname)
        self.layers = []  # list of Layer objects
        for layer in data['layers']:
            _layer = Layer(**layer)
            self.layers.append(_layer)

        self.spriteSheets = {}  # Sprite sheet image storage
        for k, v in data['spriteSheets'].items():
            self.spriteSheets[k] = strToImage(v)

        self.names = list(self.spriteSheets.keys())
        self.name_index = 0
        data.pop('layers')
        data.pop('spriteSheets')
        self.__dict__.update(data)

    def show_spriteSheet_name(self, font, screen):
        name = self.names[self.name_index]
        text = font.render(name, True, (255, 255, 255))  # White text for better visibility
        screen.blit(text, (20, 550))

    def show_fps(self, font, screen, clock):
        message = f'{clock.get_fps():.2f} FPS'
        text = font.render(message, True, (255, 255, 255))  # White text for FPS
        screen.blit(text, (800 - text.get_width(), 550))

    def draw(self, screen):
        name = self.names[self.name_index]
        screen.blit(self.spriteSheets[name], (10, 20))

    def up(self):
        self.name_index = (self.name_index + 1) % len(self.names)

    def down(self):
        self.name_index = (self.name_index - 1) % len(self.names)

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Kaitong')
font = Font('R.ttf', 24)  # Ensure the font file 'R.ttf' exists
tileset = Tileset()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [K_LEFT, K_DOWN]:
                tileset.down()
            elif event.key in [K_RIGHT, K_UP]:
                tileset.up()

    screen.fill((125, 125, 125))  # Clear screen with black
    tileset.show_spriteSheet_name(font, screen)
    tileset.show_fps(font, screen, clock)
    tileset.draw(screen)  # Optionally, add logic to draw tiles here
    clock.tick(60)  # Limit FPS to 60
    pygame.display.flip()

pygame.quit()
