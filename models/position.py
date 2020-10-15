#! /usr/bin/python
# from .labyrinth import Labyrinth
from events.switch import Event
from startgame import StartChoice

class Position:
    """Define the player's position in the labyrinth."""


    def __init__(self, x, y):
        self.position = (x,y)

    @staticmethod
    def get_event(event):
        return event.val

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    def __getitem__(self, key):
        return self.position[key]

    def up(self):
        e = Event()
        switched = e.setval
        pos_x, pos_y = self.position
        return Position(pos_x, pos_y-switched)

    def down(self):
        e = Event()
        switched = e.setval
        pos_x, pos_y = self.position
        return Position(pos_x, pos_y+switched)

    def right(self):
        e = Event()
        switched = e.setval
        pos_x, pos_y = self.position
        return Position(pos_x+switched, pos_y)

    def left(self):
        e = Event()
        switched = e.setval
        pos_x, pos_y = self.position
        return Position(pos_x-switched, pos_y)


