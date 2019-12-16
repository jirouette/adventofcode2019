#!/usr/bin/python3
#coding: utf8
from intcode import IntcodeEngine
from part1 import DrawingRobot

if __name__ == '__main__':
    engine = IntcodeEngine('input', interactive=False)
    robot = DrawingRobot(engine, start_color=1)
    robot.run()
    min_y = min(robot.grid.keys())
    min_x = 0
    max_y = max(robot.grid.keys())
    max_x = 0
    for line in robot.grid.values():
        min_line = min(line.keys())
        max_line = max(line.keys())
        if min_line < min_x:
            min_x = min_line
        if max_line > max_x:
            max_x = max_line

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            px = ['.','#'][robot.grid.get(y, dict()).get(x, 0)]
            print(px, end="")
        print()
