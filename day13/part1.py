#!/usr/bin/python3
#coding: utf8
from intcode import IntcodeEngine

class Arcade:
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4

    def __init__(self, engine):
        self.grid = {}
        self.engine = engine

    def run(self):
        self.engine.run()
        while not self.engine.is_halted:
            x = self.engine.get_output()
            self.engine.run() # resume running after previous output
            y = self.engine.get_output()
            self.engine.run() # resume running after previous output
            tile_id = self.engine.get_output()
            self.draw(x, y, tile_id)
            self.engine.run()

    def draw(self, x, y, tile_id):
        if y not in self.grid:
            self.grid[y] = {}
        self.grid[y][x] = tile_id

if __name__ == '__main__':
    engine = IntcodeEngine('input', interactive=False)
    arcade = Arcade(engine)
    arcade.run()
    nb_block = 0
    for line in arcade.grid.values():
        for tile in line.values():
            nb_block += int(tile == Arcade.BLOCK)
    print(nb_block)

