#!/usr/bin/python3
#coding: utf8
from intcode import IntcodeEngine
from part1 import Arcade
import tty, sys, termios
import json

class FunctionalArcade(Arcade):
    TILES = {
        Arcade.EMPTY: ' ',
        Arcade.WALL: '█',
        Arcade.BLOCK: '\33[34m▓\033[0m',
        Arcade.HORIZONTAL_PADDLE: '═',
        Arcade.BALL: '\33[32m•\033[0m'
    }

    def __init__(self, engine):
        super().__init__(engine)
        self.score = 0

    def draw(self, x, y, tile_id):
        if x == -1 and y == 0:
            # updating score
            self.score = tile_id
        else:
            super().draw(x,y,tile_id)

    def print(self):
        min_y = min(self.grid.keys())
        min_x = 0
        max_y = max(self.grid.keys())
        max_x = 0
        for line in self.grid.values():
            min_line = min(line.keys())
            max_line = max(line.keys())
            if min_line < min_x:
                min_x = min_line
            if max_line > max_x:
                max_x = max_line

        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                px = FunctionalArcade.TILES[self.grid.get(y, dict()).get(x, 0)]
                print(px, end="")
            print()
        print("SCORE : %010d"%self.score)

    def savestate(self, name):
        state = {
            "intcode.memory": self.engine.memory,
            "intcode.pointer": self.engine.pointer-1, # current opcode
            "intcode.relative_base": self.engine.relative_base,
            "arcade.grid": self.grid,
            "arcade.score": self.score
        }
        json.dump(state, open(name+'.savestate', 'w'))

    def loadstate(self, name):
        state = json.load(open(name+'.savestate'))
        self.engine.memory = {int(k): int(v) for k, v in state['intcode.memory'].items()}
        self.engine.pointer = state['intcode.pointer']
        self.engine.relative_base = state['intcode.relative_base']
        self.grid = {int(y): {int(x): int(tile) for x, tile in line.items()} for y, line in state['arcade.grid'].items()}
        self.score = state['arcade.score']

def input_int(placeholder, abort=False):
    while not abort:
        try:
            return int(input(placeholder))
        except ValueError:
            if not abort:
                print("Erroneous value, please retry")
    return False

def joystick():
    print(chr(27) + "[2J") # clear
    arcade.print()
    # https://stackoverflow.com/a/510364
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        while True:
            ch = ord(sys.stdin.read(1))
            if ch in [27,91]:
                continue
            if ch == 65: # UP
                # saving savestate
                arcade.savestate('0')
                print('saved state!')
                continue
            elif ch == 68: # LEFT
                ch = -1
            elif ch == 67: # RIGHT
                ch = 1
            else:
                ch = 0 # NEUTRAL
            break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == '__main__':
    engine = IntcodeEngine('input', interactive=joystick)
    engine.memory[0] = 2 # let's play for free!
    arcade = FunctionalArcade(engine)
    if input('Load state? (y/N)') == 'y':
        arcade.loadstate('0')
    arcade.run()
    print("FINAL SCORE : %010d"%arcade.score)