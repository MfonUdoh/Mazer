import os


class game(object):
    
    def __init__(self):
      self.size = 10

    def set_level(self,level):
      levels = {
        1 : [
      [3,0],[0,7],[2,2], [0,4], [4,4], [4,3], [9,5], [4,9], [9,7], [5,4], [4,0], [9,6], [4,5], [4,6], [3,6], [8,7], [4, 2]
      ]
      }
      playerpos = {
        1 : [3,5]
      }
      walls.locations = levels[level]
      player.position_x = playerpos[level][0]
      player.position_y = playerpos[level][1]
      walls.count = len(walls.locations)

    
    def print_board(self, playx, playy):
        os.system('clear')
        print("Marks remaining: " + str((game.size ** 2) - walls.count - marks.count))
        print("Turns taken: " + str(player.turns))
        hline = "".join(['_']*(game.size * 6 + 1))
        locs = []
        
        for row in range(self.size):
            y = row
            addition = []
            for col in range((self.size + 1)*2):
                x = int(col / 2 - 0.5)
                cord = [x,y]
                if col % 2 == 0:
                    if col == 0 or x == self.size - 1:
                        addition.append("|")
                    else:
                        addition.append(" ")
                elif playy == y and playx == x:
                    addition.append("O")
                elif cord in marks.locations:
                    addition.append(".")
                elif cord in walls.locations:
                    addition.append("X")
                else:
                    addition.append(" ")
            locs.append(addition)
        
        print(hline)
        for row in range(self.size):
            print()
            print("  ".join(locs[row]))
        print(hline)


class player(object):
    
    def __init__(self):
        
        self.position_x = 0
        self.position_y = 0
        self.turns = 0
        
    def distance_to_edge(self, direction, walls):
        
        calc = []
        edge = 0
        
        for wall in walls:
            
            if direction == 'd':
                edge = (game.size - 1) - self.position_x
                if wall[1] == self.position_y and (wall[0] - self.position_x) > 0:
                    calc.append(wall[0] - self.position_x)
                    
            elif direction == 'a':
                edge = self.position_x
                if wall[1] == self.position_y and (self.position_x - wall[0]) > 0:
                    calc.append(self.position_x - wall[0])
                    
            elif direction == 's':
                edge = (game.size - 1) - self.position_y
                if wall[0] == self.position_x and (wall[1] - self.position_y) > 0:
                    calc.append(wall[1] - self.position_y)
                    
            elif direction == 'w':
                edge = self.position_y
                if wall[0] == self.position_x and (self.position_y - wall[1]) > 0:
                    calc.append(self.position_y - wall[1])
                    

        if calc == []:
            calc = edge
        else:
            calc = min(calc)-1
        return calc
              
    def move(self, direction):
        
        xpos1 = self.position_x
        ypos1 = self.position_y
        xpos2 = xpos1
        ypos2 = ypos1
        skip = self.distance_to_edge(direction, walls.locations)
        moves = {
            'a' : [-skip , 0],
            'd' : [skip , 0],
            'w' : [0 , -skip],
            's' : [0 , skip]
        }
        
        if \
            direction in moves \
            and self.position_x + moves[direction][0] in range(game.size) \
            and self.position_y + moves[direction][1] in range(game.size):
            self.position_x += moves[direction][0]
            self.position_y += moves[direction][1]
            xpos2 = self.position_x
            ypos2 = self.position_y
            self.turns += 1
        marks.make(xpos1, xpos2, ypos1, ypos2)


class walls(object):
    
    def __init__(self):
        
        self.locations = []
        self.count = 0
    
    


class marks(object):

    def __init__(self):
        
        self.locations = []
        self.count = len(self.locations)

    def make(self, xpos1, xpos2, ypos1, ypos2):
        
        if ypos1 == ypos2 and xpos2 > xpos1:
            for displace in range(xpos2 - xpos1 + 1):
                if [xpos1 + displace, ypos1] not in self.locations:
                    self.locations.append([xpos1 + displace, ypos1])
        elif ypos1 == ypos2 and xpos1 > xpos2:
            for displace in range(xpos1 - xpos2 + 1):
                if [xpos2 + displace, ypos1] not in self.locations:
                    self.locations.append([xpos2 + displace, ypos1])
        elif ypos2 > ypos1:
            for displace in range(ypos2 - ypos1 + 1):
                if [xpos1, ypos1 + displace] not in self.locations:
                    self.locations.append([xpos1, ypos1 + displace])
        else:
            for displace in range(ypos1 - ypos2 + 1):
                if [xpos1, ypos2 + displace] not in self.locations:
                    self.locations.append([xpos1, ypos2 + displace])
        self.count = len(self.locations)

game = game()
player = player()
walls = walls()
marks = marks()

print("Welcome To MAZER")
print("Hello player, you are playing as a photon in a lazer beam, meaning you can only travel straight on until either an edge or wall (X) stops you.")
print("You must light every empty space in the maze to win, use 'w''a''s''d' keys to choose your direction of travel, up, left, down, right and press enter to move.")
print("Hit enter to continue.")
input()
game.set_level(1)
while (game.size ** 2) - walls.count - marks.count != 0:
        game.print_board(player.position_x, player.position_y)
        player.move(input())

game.print_board(player.position_x, player.position_y)
if player.turns > 145:
  player.turns = 145
print("Congrats you won the game!!!")
print("Your score " + str(100-(player.turns-45)))
print(".... Next Level?")
