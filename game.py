import sys
import random

import pygame

from pygame.locals import QUIT

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

ASSETS_PATH = './assets/'

tilemap = [[WATER for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

for row in range(MAPHEIGHT):
    for col in range(MAPWIDTH):
        random_number = random.randint(0, 15)
        tile = tilemap[row][col]

        if random_number == 0:
            tile = COAL
        elif random_number == 1 or random_number == 2:
            tile = DIRT
        elif random_number >= 3 and random_number <= 7:
            tile = GRASS

        tilemap[row][col] = tile

textures = {
    DIRT: pygame.image.load(ASSETS_PATH + 'dirt.png'),
    GRASS: pygame.image.load(ASSETS_PATH + 'grass.png'),
    WATER: pygame.image.load(ASSETS_PATH + 'water.jpeg'),
    COAL: pygame.image.load(ASSETS_PATH + 'coal.jpg')
}

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

pygame.display.set_caption('Test')

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(textures[tilemap[row][column]],
                                 (column*TILESIZE, row*TILESIZE))

    pygame.display.update()