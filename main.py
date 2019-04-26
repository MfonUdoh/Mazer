import os


class game(object):
    
    def __init__(self):
      #Board width
      self.size = 10
      self.minmoves = 0

    def set_level(self,level):
      """Assigns the location of all the walls and starting player position for the selected level"""
      
      levels = {
        1 : [
          [0,4], [0,7], [2,2], [3,0], [3,6], [4,0], [4,3], [4,2], [4,4], [4,5], [4,6], [4,9], [5,4], [8,7], [9,5],[9,6], [9,7]
      ],
        2 : [
          [0,4], [0,0], [0,9], [2,3], [2,4], [2,6], [3,6], [3,0], [4,0], [4,4], [4,6], [4,9], [5,4], [6,2], [6,6], [8,7], [7,5],[7,6], [7,7], [9,0], [9,3]
        ],
        3 : [
          [0,0], [0,1], [0,7], [0,6], [1,0], [1,3], [2,2], [3,7], [3,9], [4,2], [4,5], [4,6], [4,9], [5,0], [5,1], [5,2], [5,9], [6,5], [8,0], [8,8], [9,0], [9,1], [9,4], [9,5]
        ],
        4 : [
          [0,3], [0,7], [0,8], [0,9], [1,1], [1,9], [2,1], [2,5], [2,7], [2,9], [3,5], [3,9], [4,0], [4,4], [4,5], [5,9], [7,0], [8,6], [9,4],[9,5], [9,6], [9,9]
        ],
        0 : [
          [0,0], [0,1], [0,2], [0,3], [0,4], [0,6], [0,7], [0,8], [0,9], [1,0], [1,6], [1,7], [1,9], [2,0], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7], [2,9], [3,0], [3,4], [4,0], [4,1], [4,2], [4,4], [4,6], [4,7], [5,0], [5,1], [5,2], [5,6], [5,7], [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [7,0], [7,7], [7,9], [8,0], [8,9], [9,0], [9,1], [9,2], [9,3], [9,4], [9,5], [9,6], [9,7], [9,8], [9,9]
        ]
      }
      playerpos = {
        1 : [3,5],
        2 : [3,2],
        3 : [9,9],
        4 : [4,9],
        0 : [1,8]
      }
      minmoves = {
        1 : 43,
        2 : 45,
        3 : 40,
        4 : 32,
        0 : 15
      }
      self.minmoves = minmoves[level]
      walls.locations = levels[level]
      player.position_x = playerpos[level][0]
      player.position_y = playerpos[level][1]
      walls.count = len(walls.locations)
      marks.locations = []
      marks.count = 0
      player.turns = 0

    
    def print_board(self, playx, playy):
        """Displays the game board"""
        os.system('clear')
        print ("LEVEL " + str(lvl))
        print("Empty Spaces Remaining: " + str((game.size ** 2) - walls.count - marks.count))
        print("Turns Taken: " + str(player.turns))
        
        hline = "".join(['_']*(game.size * 6 + 1))
        locs = []
        for row in range(self.size):
            y = row
            addition = []
            for col in range((self.size + 1)*2):
                #for each row if statements decide which element to fill a space with or leave it blank
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
        """Calculates how far away the nearest wall or edge is and returns how far the player must travel to get there"""
        calc = []
        edge = 0
        
        for wall in walls:
            #I think I can simply the logic here
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
        """Takes a direction and moves the player in that direction"""
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
            #if statement checks the move is in still in the maze and is a legal direction
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
        """Creates markers at every position that the player crosses"""
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
lvl = 0
scores = []
while lvl <= 4:
    game.set_level(lvl)
    while (game.size ** 2) - walls.count - marks.count != 0:
            game.print_board(player.position_x, player.position_y)
            player.move(input())

    game.print_board(player.position_x, player.position_y)
    if player.turns > 100 + game.minmoves:
      player.turns = 100 + game.minmoves
    print("Congrats you completed the maze!!!")
    score = 100-(player.turns-game.minmoves)
    scores.append(score)
    print("Your score " + str(score))
    print(".... Next Level?")
    input()
    lvl += 1
os.system('clear')
totalscore = sum(scores)
print("Congratulations looks like you have illuminated all of the mazes!!!")
print("Your total score is: " + str(totalscore) + " out of 500")
