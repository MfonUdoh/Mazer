class Game(object):

    def __init__(self):
        #Board width
        self.size = 10
        self.minMoves = 0
        self.level = 0
        self.empties = 0
        self.marksLocations = []
        self.wallsLocations = []
        self.maxLevels = 0
        self.x1 = 0
        self.y1 = 0
        self.x2= 0
        self.y2 = 0
        self.turns = 0

    def set_level(self, level):
        """Assigns the location of all the walls and starting player position for the selected level"""
        self.minmoves = level.minMoves[self.level]
        self.wallsLocations = level.wallLocations[self.level]
        self.marksLocations = []
        self.maxLevels = len(level.minMoves) - 1
        self.x1, self.x2 = level.playerPosition[self.level][0]
        self.y1, self.y2 = level.playerPosition[self.level][1]

    def render_board(self, x, y, marks, walls, turns):
        pass
    
    def make_marks(self, xpos1, xpos2, ypos1, ypos2):
        """Creates markers at every position that the player crosses"""
        if ypos1 == ypos2 and xpos2 > xpos1:
            for displace in range(xpos2 - xpos1 + 1):
                if [xpos1 + displace, ypos1] not in self.marksLocations:
                    self.marksLocations.append([xpos1 + displace, ypos1])
        elif ypos1 == ypos2 and xpos1 > xpos2:
            for displace in range(xpos1 - xpos2 + 1):
                if [xpos2 + displace, ypos1] not in self.marksLocations:
                    self.marksLocations.append([xpos2 + displace, ypos1])
        elif ypos2 > ypos1:
            for displace in range(ypos2 - ypos1 + 1):
                if [xpos1, ypos1 + displace] not in self.marksLocations:
                    self.marksLocations.append([xpos1, ypos1 + displace])
        else:
            for displace in range(ypos1 - ypos2 + 1):
                if [xpos1, ypos2 + displace] not in self.marksLocations:
                    self.marksLocations.append([xpos1, ypos2 + displace])
        self.count = len(self.marksLocations)
        return self.marksLocations, self.count
