import levels, pygame, game
from player import *
from pygame.locals import *

game = game.Game()

running = True
end = False


pygame.init()
screen_width = 600
screen_height = 600
multiple = 50
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mazer")
radius = int(0.25 * multiple)
wallwidth = int(0.50 * multiple)
markradius = int(0.05 * multiple)
scores = []


while running:
    playing = True
    pygame.time.delay(1000)
    game.set_level(levels)
    x = multiple * (game.x1 + 1) + radius
    y = multiple * (game.y1 + 1) + radius
    font = pygame.font.SysFont(None, 20)

    screen.fill((0, 0, 0))
    textSurface = font.render("LEVEL: {}    TURNS: {}    EMPTY SPACES: {}".format(game.level, game.turns, game.empties), True, [255, 255, 255], [0, 0, 0])
    screen.blit(textSurface, (int(0.2 * multiple), int(0.3 * multiple)))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius, )
    for wall in game.wallsLocations:
        pygame.draw.rect(screen, (255, 255, 255), (int(multiple * (1 + wall[0])), int(multiple * (1 + wall[1])), wallwidth, wallwidth))
    
    pygame.display.update()

    while playing:
        pygame.time.delay(10)
        refresh = False
        keys = pygame.key.get_pressed()
        if game.empties != 0:
            if keys[pygame.K_LEFT or pygame.K_a]:
                # Can make it only refresh if the move returns true
                game.move('a')
                refresh = True
            elif keys[pygame.K_RIGHT or pygame.K_d]:
                game.move('d')
                refresh = True
            elif keys[pygame.K_UP or pygame.K_w]:
                game.move('w')
                refresh = True
            elif keys[pygame.K_DOWN or pygame.K_s]:
                game.move('s')
                refresh = True
        else:
            if game.turns > 100 + game.minMoves:
                game.turns = 100 + game.minMoves
            scores.append(100-(game.turns-game.minMoves))
            game.level += 1
            if game.level >= game.maxLevels:
                end = True
            break
        if refresh:
            game.make_marks()
            x = multiple * (game.x1 + 1) + radius
            y = multiple * (game.y1 + 1) + radius

            screen.fill((0, 0, 0))
            textSurface = font.render("LEVEL: {}    TURNS: {}    EMPTY SPACES: {}".format(game.level, game.turns, game.empties), True, [255, 255, 255], [0, 0, 0])
            screen.blit(textSurface, (int(0.2 * multiple), int(0.3 * multiple)))
            for mark in game.marksLocations:
                pygame.draw.circle(screen, (255, 255, 255), (int(multiple * (1.25 + mark[0])), int(multiple * (1.25 + mark[1]))), markradius)
            pygame.draw.circle(screen, (255, 255, 0), (x, y), radius, )
            for wall in game.wallsLocations:
                pygame.draw.rect(screen, (255, 255, 255), (int(multiple * (1 + wall[0])), int(multiple * (1 + wall[1])), wallwidth, wallwidth))
            pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                running = False
    if end:
        totalscore = sum(scores)
        screen.fill((0, 0, 0))
        textSurface = font.render("Congratulations, you have completed the game!", True, [255, 255, 255], [0, 0, 0])
        screen.blit(textSurface, (int(0.2 * multiple), int(0.3 * multiple)))
        scoreSurface = font.render("Final Score: {}".format(totalscore), True, [255, 255, 255], [0, 0, 0])
        screen.blit(scoreSurface, (int(5 * multiple), int(5 * multiple)))
        pygame.display.update()
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    end = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

# scores = player.player().run_game()
# os.system('clear')
# totalscore = sum(scores)
# print("Congratulations looks like you have illuminated all of the mazes!!!")
# print("Your total score is: " + str(totalscore) + " out of 500") # change to vary based on number of levels
