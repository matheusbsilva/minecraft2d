import sys
import random

import pygame

from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

ASSETS_PATH = './assets/'

tilemap = [[WATER for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
inventory = {
        DIRT: 0,
        GRASS: 0,
        WATER: 0,
        COAL: 0
    }

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

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))
PLAYER = pygame.image.load(ASSETS_PATH + 'player.png').convert_alpha()
player_pos = [0, 0]

pygame.display.set_caption('Test')

while True:

    for event in pygame.event.get():
        print("[EVENT]", event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_tile = tilemap[player_pos[1]][player_pos[0]]
                inventory[current_tile] += 1
                tilemap[player_pos[1]][player_pos[0]] = DIRT
                print('[INVENTORY]', inventory)
            elif event.key == pygame.K_RIGHT and player_pos[0] < MAPWIDTH - 1:
                player_pos[0] += 1
            elif event.key == pygame.K_LEFT and player_pos[0] > 0:
                player_pos[0] -= 1
            elif event.key == pygame.K_UP and player_pos[1] > 0:
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN and player_pos[1] < MAPHEIGHT - 1:
                player_pos[1] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]],
                             (column*TILESIZE, row*TILESIZE))

    DISPLAYSURF.blit(PLAYER,
                     (player_pos[0]*TILESIZE, player_pos[1]*TILESIZE))

    pygame.display.update()
