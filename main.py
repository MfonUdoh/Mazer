import levels, pygame, game
from player import *
from pygame.locals import *

game = game.Game()
# x = multiple * (levels.playerpos[game.lvl][0] + 1) + radius
# y = multiple * (levels.playerpos[game.lvl][1] + 1) + radius

running = True

while running:
    game.set_level(levels)
    game.empties = (game.size ** 2) - len(game.wallsLocations) - len(game.marksLocations)
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

    while playing:

        if game.empties != 0:
            if keys[pygame.K_LEFT or pygame.K_a]:
                playeri.move('a')
                marksi.make(playeri.position_x, playeri.next_position_x, playeri.position_y, playeri.next_position_y)
                game.render_board(playeri.position_x, playeri.position_x, marksi.locations)
            elif keys[pygame.K_RIGHT or pygame.K_d]:
                playeri.move('d')
                game.render_board()
            elif keys[pygame.K_UP or pygame.K_w]:
                playeri.move('w')
                game.render_board()
            elif keys[pygame.K_DOWN or pygame.K_s]:
                playeri.move('s')
                game.render_board()
            
        else:
            game.lvl += 1
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# while running:
    
#     x1 = playeri.position_x
#     x2 = playeri.position_x
#     y1 = playeri.position_y
#     y2 = playeri.position_y

#     walls.locations = levels.levels[game.lvl]
#     walls.count = len(walls.locations)
#     pygame.time.delay(10)
#     game.empties = (game.size ** 2) - walls.count - marksi.count
#     keys = pygame.key.get_pressed()

#     if game.empties == 0:
#         # myfont.Font.render('Next Level', 1, (255, 100, 100))
#         if game.lvl == game.maxlevels:
#             running = False
#         else:
#             game.lvl += 1
#             playeri.position_x = levels.playerpos[game.lvl][0]
#             playeri.position_y = levels.playerpos[game.lvl][1]
#             x = multiple * (levels.playerpos[game.lvl][0] + 1) + radius
#             y = multiple * (levels.playerpos[game.lvl][1] + 1) + radius
#             marksi.locations = []
#             marksi.count = 0
#             pygame.time.delay(10)
#     else:
#         if keys[pygame.K_LEFT or pygame.K_a]:
#             skip = playeri.distance_to_edge('a', levels.levels[game.lvl]) * multiple
#             if x - radius - skip >= 0:
#                 x -= skip
#         elif keys[pygame.K_RIGHT or pygame.K_d]:
#             skip = playeri.distance_to_edge('d', levels.levels[game.lvl]) * multiple
#             if x + radius + skip <= screen_width:
#                 x += skip
#         elif keys[pygame.K_UP or pygame.K_w]:
#             skip = playeri.distance_to_edge('w', levels.levels[game.lvl]) * multiple
#             if y - radius - skip >= 0:
#                 y -= skip
#         elif keys[pygame.K_DOWN or pygame.K_s]:
#             skip = playeri.distance_to_edge('s', levels.levels[game.lvl]) * multiple
#             if y + radius + skip <= screen_height:
#                 y += skip

#         playeri.turns += 1
#         playeri.position_x = int(((x - radius) / multiple) - 1)
#         playeri.position_y = int(((y - radius) / multiple) - 1)
        
#         x2 = playeri.position_x
#         y2 = playeri.position_y

#         marksi.make(x1, x2, y1, y2)
        
#         screen.fill((0, 0, 0))

#         font = pygame.font.SysFont(None, 20)
#         textSurface = font.render("LEVEL: {}    TURNS: {}    EMPTY SPACES: {}".format(game.lvl, playeri.turns, game.empties), True, [255, 255, 255], [0, 0, 0])
#         screen.blit(textSurface, (int(0.2 * multiple), int(0.3 * multiple)))

#         for mark in marksi.locations:
#             pygame.draw.circle(screen, (255, 255, 255), (int(multiple * (1.25 + mark[0])), int(multiple * (1.25 + mark[1]))), markradius)
#         pygame.draw.circle(screen, (255, 255, 0), (x, y), radius, )
#         for wall in levels.levels[game.lvl]:
#             pygame.draw.rect(screen, (255, 255, 255), (int(multiple * (1 + wall[0])), int(multiple * (1 + wall[1])), wallwidth, wallwidth))
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.update()

pygame.quit()

# scores = player.player().run_game()
# os.system('clear')
# totalscore = sum(scores)
# print("Congratulations looks like you have illuminated all of the mazes!!!")
# print("Your total score is: " + str(totalscore) + " out of 500") # change to vary based on number of levels
