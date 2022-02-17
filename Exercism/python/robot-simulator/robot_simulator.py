NORTH, EAST, SOUTH, WEST = range(4)


class Robot:

    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y

    def advance(self):
        self.x += (0, 1, 0, -1)[self.direction]
        self.y += (1, 0, -1, 0)[self.direction]

    @property
    def coordinates(self): return self.x, self.y
    def turn(self, i): self.direction = (self.direction + i) % 4
    def move(self, commands: str): [RUN[c](self) for c in commands.upper()]
    def turn_right(self): return self.turn(1)
    def turn_left(self): return self.turn(-1)


RUN = {'A': Robot.advance, 'R': Robot.turn_right, 'L': Robot.turn_left}
