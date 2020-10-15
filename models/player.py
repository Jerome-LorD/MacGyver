#! /usr/bin/python
from .position import Position
from .labyrinth import Labyrinth

class Player:
    def __init__(self, struct):

        self.struct = struct
        self.position = self.struct.start

    def move(self, direction):
        directions = ["up", "down", "right", "left"]
        if direction not in directions:
            pass
        else:
            new_position = getattr(self.position, direction)()
            if new_position in self.struct:
                self.position = new_position
            return self.position


