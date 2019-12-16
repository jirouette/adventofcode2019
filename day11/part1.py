#!/usr/bin/python3
#coding: utf8
from intcode import IntcodeEngine


class DrawingRobot:
    BLACK = 0
    WHITE = 1
    DIRECTIONS = ['UP', 'RIGHT', 'DOWN', 'LEFT']

    def __init__(self, engine, start_color=0):
        self.grid = {}
        self.x = 0
        self.y = 0
        self.direction = 0
        self.drawn_panels = 0
        self.engine = engine
        self.engine.add_input(start_color)

    def run(self):
        self.engine.run()
        while not self.engine.is_halted:
            color = self.engine.get_output()
            self.draw(color)
            self.engine.run() # resume running after previous output
            direction = self.engine.get_output()
            self.direction += [-1, 1][direction]
            self.direction %= len(DrawingRobot.DIRECTIONS)
            self.move()
            self.engine.add_input(self.get_current_color())
            self.engine.run()

    def draw(self, color):
        if self.y not in self.grid:
            self.grid[self.y] = {}
        if self.x not in self.grid[self.y]:
            self.drawn_panels += 1
        self.grid[self.y][self.x] = color

    def move(self):
        direction = DrawingRobot.DIRECTIONS[self.direction]
        if direction == 'UP':
            self.y -= 1
        elif direction == 'DOWN':
            self.y += 1
        elif direction == 'RIGHT':
            self.x += 1
        else:
            self.x -= 1

    def get_current_color(self):
        return self.grid.get(self.y, dict()).get(self.x, 0)

if __name__ == '__main__':
    engine = IntcodeEngine('input', interactive=False)
    robot = DrawingRobot(engine)
    robot.run()
    print(robot.drawn_panels)
