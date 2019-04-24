#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os


# In[ ]:


class game(object):
    
    def __init__(self):
        pass
    
    def print_board(playx, playy):
        os.system('clear')
        hline = "".join(['_']*31)
        locs = []
        
        for row in range(5):
            y = row
            addition = []
            for col in range(11):
                x = int(col / 2 - 0.5)
                cord = [x,y]
                if col % 2 == 0:
                    addition.append("|")
                elif playy == y and playx == x:
                    addition.append("X")
                elif cord in marks.locations:
                    addition.append("O")
                elif cord in walls.locations:
                    addition.append("H")
                else:
                    addition.append(" ")
            locs.append(addition)
        print(hline)
        for row in range(5):
            print()
            print("  ".join(locs[row]))
            print(hline)




# In[ ]:


class player(object):
    
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        
    def distance_to_edge(self, direction, walls):
        calc = []
        edge = 0
        for wall in walls:
            if direction == 'd':
                edge = 4 - self.position_x
                if wall[1] == self.position_y and (wall[0] - self.position_x) > 0:
                    calc.append(wall[0] - self.position_x)
                    
            elif direction == 'a':
                edge = self.position_x
                if wall[1] == self.position_y and (self.position_x - wall[0]) > 0:
                    calc.append(self.position_x - wall[0])
                    
            elif direction == 's':
                edge = 4 - self.position_y
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
            and self.position_x + moves[direction][0] in range(5) \
            and self.position_y + moves[direction][1] in range(5):
            self.position_x += moves[direction][0]
            self.position_y += moves[direction][1]
            xpos2 = self.position_x
            ypos2 = self.position_y
        else:
            print("Move not valid, try again.")
        marks.make(xpos1, xpos2, ypos1, ypos2)


# In[ ]:


class walls(object):
    
    def __init__(self):
        self.locations = [[3,0],[2,1],[2,2], [0,4], [4,4], [4,3]]
        self.count = len(self.locations)


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


player = player()
walls = walls()
marks = marks()

# In[ ]:


while 25 - walls.count - marks.count != 0:
        game.print_board(player.position_x, player.position_y)
        player.move(input())

print("Congrats you won the game!!!")
game.print_board(player.position_x, player.position_y)


# In[ ]:




