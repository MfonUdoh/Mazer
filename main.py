import os, player, levels
import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mazer")

radius = 25
wallwidth = 50
skip = 100
x = int(100 * (levels.playerpos[0][0] + 1) + radius)
y = int(100 * (levels.playerpos[0][1] + 1) + radius)
run = True

while run:
    pygame.time.delay(100)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - radius - skip >= 0:
        x -= skip
    if keys[pygame.K_RIGHT] and x + radius + skip <= screen_width:
        x += skip
    if keys[pygame.K_UP] and y - radius - skip >= 0:
        y -= skip
    if keys[pygame.K_DOWN] and y + radius + skip <= screen_height:
        y += skip
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius, )
    for wall in levels.levels[0]:
        pygame.draw.rect(screen, (255, 255, 255), (100 * (1 + wall[0]), 100 * (1 + wall[1]), wallwidth, wallwidth))

    pygame.display.update()

pygame.quit()
# print("Welcome To MAZER")
# print("Hello player, you are playing as a photon in a lazer beam, meaning you can only travel straight on until either an edge or wall (X) stops you.")
# print("You must light every empty space in the maze to win, use 'w''a''s''d' keys to choose your direction of travel, up, left, down, right and press enter to move.")
# print("Hit enter to continue.")
# input()



# scores = player.player().run_game()
# os.system('clear')
# totalscore = sum(scores)
# print("Congratulations looks like you have illuminated all of the mazes!!!")
# print("Your total score is: " + str(totalscore) + " out of 500") # change to vary based on number of levels
