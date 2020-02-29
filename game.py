import pygame, levels, walls, marks, player
from pygame.locals import *

class Game(object):
    
    def __init__(self):
      #Board width
      self.size = 10
      self.minmoves = 0
      self.lvl = 0
      self.empties = 0
      self.maxlevels = len(levels.levels) - 1
      

    def set_level(self, levels):
      """Assigns the location of all the walls and starting player position for the selected level"""
      #Level data should be read from a seperate file
      self.minmoves = levels.minmoves[level]
      walls.locations = levels.levels[level]
      playx = levels.playerpos[level][0]
      playy = levels.playerpos[level][1]
      return playx, playy

    def render_board(self, x, y, marks, walls, turns):
        self.empties = (self.size ** 2) - walls.count - marks.count
        pygame.init()
        screen_width = 600
        screen_height = 600
        multiple = 50
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Mazer")

        radius = int(0.25 * multiple)
        wallwidth = int(0.50 * multiple)
        markradius = int(0.05 * multiple)

        screen.fill((0, 0, 0))

        font = pygame.font.SysFont(None, 20)
        textSurface = font.render("LEVEL: {}    TURNS: {}    EMPTY SPACES: {}".format(self.lvl, playeri.turns, self.empties), True, [255, 255, 255], [0, 0, 0])
        screen.blit(textSurface, (int(0.2 * multiple), int(0.3 * multiple)))

        for mark in marks.locations:
            pygame.draw.circle(screen, (255, 255, 255), (int(multiple * (1.25 + mark[0])), int(multiple * (1.25 + mark[1]))), markradius)
        pygame.draw.circle(screen, (255, 255, 0), (x, y), radius, )
        for wall in levels.levels[game.lvl]:
            pygame.draw.rect(screen, (255, 255, 255), (int(multiple * (1 + wall[0])), int(multiple * (1 + wall[1])), wallwidth, wallwidth))
        
        pygame.display.update()
