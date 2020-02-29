class player(object):
    
    def __init__(self):
        
        self.position_x = 0
        self.position_y = 0
        self.next_position_x = 0
        self.next_position_y = 0
        self.turns = 0
        
    def distance_to_edge(self, direction, walls):
        """Calculates how far away the nearest wall or edge is and returns how far the self must travel to get there"""
        calc = []
        edge = 0
        
        for wall in walls:
            #I think I can simplify the logic here
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
        
        self.position_x = self.next_position_x
        self.position_y = self.next_position_y

        skip = self.distance_to_edge(direction, walls.locations)
        moves = {
            'a' : [-skip, 0],
            'd' : [skip, 0],
            'w' : [0, -skip],
            's' : [0, skip]
        }

        if \
            direction in moves \
            and self.position_x + moves[direction][0] in range(game.size) \
            and self.position_y + moves[direction][1] in range(game.size):
            #if statement checks the move is in still in the maze and is a legal direction
            self.next_position_x = self.position_x + moves[direction][0]
            self.next_position_y = self.position_y + moves[direction][1]
            if self.next_position_x != self.position_x or self.next_position_y != self.position_y:
                self.turns += 1 
        
        return self.turns, self.position_x, self.next_position_x, self.position_y, self.next_position_y