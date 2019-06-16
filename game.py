import os, walls, levels
from marks import *
marks = marks()

class game(object):
    
    def __init__(self):
      #Board width
      self.size = 10
      self.minmoves = 0
      self.lvl = 0
      self.empties = 0
      self.maxlevels = len(levels.levels) - 1

    def set_level(self,level):
      """Assigns the location of all the walls and starting player position for the selected level"""
      #Level data should be read from a seperate file
      self.minmoves = levels.minmoves[level]
      walls.locations = levels.levels[level]
      playx = levels.playerpos[level][0]
      playy = levels.playerpos[level][1]
      walls.count = len(walls.locations)
      marks.locations = []
      marks.count = 0
      turns = 0
      return playx, playy, turns

    def print_board(self, turns, xpos1, xpos2, ypos1, ypos2):
        """Displays the game board"""
        os.system('clear')
        marks.make(xpos1, xpos2, ypos1, ypos2)
        self.empties = (self.size ** 2) - walls.count - marks.count
        print ("LEVEL " + str(self.lvl))
        print("Empty Spaces Remaining: " + str(self.empties) )
        print("Turns Taken: " + str(turns))
        hline = "".join(['_']*(self.size * 6 + 1))
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
                elif xpos2 == x and ypos2 == y:
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
