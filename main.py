import os, levels, pygame

from player import *
from pygame.locals import *
from marks import *
from walls import *
walls = walls()
marksi = marks()
pygame.init()
playeri = player()
# game.lvl = 4
screen_width = 600
screen_height = 600
multiple = 50
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mazer")

radius = int(0.25 * multiple)
wallwidth = int(0.50 * multiple)
markradius = int(0.05 * multiple)

x = multiple * (levels.playerpos[game.lvl][0] + 1) + radius
y = multiple * (levels.playerpos[game.lvl][1] + 1) + radius

playeri.position_x = levels.playerpos[game.lvl][0]
playeri.position_y = levels.playerpos[game.lvl][1]
run = True

while run:
    
    x1 = playeri.position_x
    x2 = playeri.position_x
    y1 = playeri.position_y
    y2 = playeri.position_y

    walls.locations = levels.levels[game.lvl]
    walls.count = len(walls.locations)
    pygame.time.delay(100)
    game.empties = (game.size ** 2) - walls.count - marksi.count
    keys = pygame.key.get_pressed()

    if game.empties == 0:
        # myfont.Font.render('Next Level', 1, (255, 100, 100))
        if game.lvl == game.maxlevels:
            run = False
        else:
            game.lvl += 1
            playeri.position_x = levels.playerpos[game.lvl][0]
            playeri.position_y = levels.playerpos[game.lvl][1]
            x = multiple * (levels.playerpos[game.lvl][0] + 1) + radius
            y = multiple * (levels.playerpos[game.lvl][1] + 1) + radius
            marksi.locations = []
            marksi.count = 0

    else:
        if keys[pygame.K_LEFT]:
            skip = playeri.distance_to_edge('a', levels.levels[game.lvl]) * multiple
            if x - radius - skip >= 0:
                x -= skip
        if keys[pygame.K_RIGHT]:
            skip = playeri.distance_to_edge('d', levels.levels[game.lvl]) * multiple
            if x + radius + skip <= screen_width:
                x += skip
        if keys[pygame.K_UP]:
            skip = playeri.distance_to_edge('w', levels.levels[game.lvl]) * multiple
            if y - radius - skip >= 0:
                y -= skip
        if keys[pygame.K_DOWN]:
            skip = playeri.distance_to_edge('s', levels.levels[game.lvl]) * multiple
            if y + radius + skip <= screen_height:
                y += skip

        # print ("LEVEL " + str(game.lvl))
        # print("Empty Spaces Remaining: " + str(game.empties) )
        # print("Turns Taken: " + str(turns))
        
        playeri.position_x = int(((x - radius) / multiple) - 1)
        playeri.position_y = int(((y - radius) / multiple) - 1)
        
        x2 = playeri.position_x
        y2 = playeri.position_y

        marksi.make(x1, x2, y1, y2)
        
        screen.fill((0, 0, 0))
        for mark in marksi.locations:
            pygame.draw.circle(screen, (255, 255, 255), (int(multiple * (1.25 + mark[0])), int(multiple * (1.25 + mark[1]))), markradius)
        pygame.draw.circle(screen, (255, 255, 0), (x, y), radius, )
        for wall in levels.levels[game.lvl]:
            pygame.draw.rect(screen, (255, 255, 255), (int(multiple * (1 + wall[0])), int(multiple * (1 + wall[1])), wallwidth, wallwidth))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

# scores = player.player().run_game()
# os.system('clear')
# totalscore = sum(scores)
# print("Congratulations looks like you have illuminated all of the mazes!!!")
# print("Your total score is: " + str(totalscore) + " out of 500") # change to vary based on number of levels
