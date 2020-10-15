#! /usr/bin/python
import config.settings as constants
from models.position import Position
# from events.switch import Event
import random
from random import choice

class Labyrinth:
    """doc str"""
    def __init__(self, file, event):
        self.file = file
        self.switched = event

        self._coord_let = []
        self.coords_wall = []
        self.coords_road = []
        self._coords_start = []
        self.coords_finnish = []
        self.tools = []
        self.toolbox = []

        self.load_structure()
        

    @property
    def struct(self):
        return self._coord_let

    @property
    def wall_lst(self):
        return self.coords_wall

    @property
    def start(self):
        return list(self._coords_start)[0]

    @property
    def finnish(self):
        return list(self.coords_finnish)[0]

    @property
    def tools_rand(self):
        return self.random_tools()

    def __contains__(self, position):
        return position in self.coords_road

    def collide_gatekeeper(self, position):
        return position in self.coords_finnish

    def collide_tube(self, position):
        return position in tuple(self.tools_rand)[0]

    def collide_needle(self, position):
        return position in tuple(self.tools_rand)[1]

    def collide_ether(self, position):
        return position in tuple(self.tools_rand)[2]

    def load_structure(self):
        # e = Event()
        # switched = e.setval
        # switched = Event.setval
        print(self.switched)

        with open("data/levels/"+self.file) as levels:
            for line in levels:
                self._coord_let.append(line.strip('\n'))
        for i in range(15):
            for k,v in enumerate(self._coord_let[i]):
                if v == constants.WALL_CHAR:
                    self.coords_wall.append((k*self.switched, i*self.switched))
                elif v == constants.ROAD_CHAR:
                    self.coords_road.append(Position(k*self.switched, i*self.switched))
                elif v == constants.START_CHAR:
                    self._coords_start.append(Position(k*self.switched, i*self.switched))
                    self.coords_road.append(Position(k*self.switched, i*self.switched))
                elif v == constants.FINNISH_CHAR:
                    self.coords_road.append(Position(k*self.switched, i*self.switched))
                    self.coords_finnish.append(Position(k*self.switched, i*self.switched))
                    print(self.switched)


    def random_tools(self):
        for i in range(3):
            self.tools.append(random.choices(self.coords_road[15:110],\
                 weights=None, cum_weights=None, k=1))
            if i == 3:
                break
        return self.tools

# def main():
#     e = Event()
#     switched = e.setval
#     print(switched)

# if __name__ == "__main__":
#     main()
