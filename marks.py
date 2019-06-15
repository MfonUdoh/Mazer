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
        return self.locations, self.count