#!/usr/bin/python3
#coding: utf8
from intcode import IntcodeEngine


class DrawingRobot:
    BLACK = 0
    WHITE = 1
    DIRECTIONS = ['UP', 'RIGHT', 'DOWN', 'LEFT']

    def __init__(self, engine):
        self.grid = {}
        self.x = 0
        self.y = 0
        self.direction = 0
        self.drawn_panels = 0
        engine.add_input(0)

    def run(self):
        engine.run()
        while not engine.is_halted:
            color = engine.get_output()
            self.draw(color)
            engine.run() # resume running after previous output
            direction = engine.get_output()
            self.direction += [-1, 1][direction]
            self.direction %= len(DrawingRobot.DIRECTIONS)
            self.move()
            engine.add_input(self.get_current_color())
            engine.run()

    def draw(self, color):
        if self.x not in self.grid:
            self.grid[self.x] = {}
        if self.y not in self.grid[self.x]:
            self.drawn_panels += 1
        self.grid[self.x][self.y] = color

    def move(self):
        direction = DrawingRobot.DIRECTIONS[self.direction]
        if direction == 'UP':
            self.y += 1
        elif direction == 'DOWN':
            self.y -= 1
        elif direction == 'RIGHT':
            self.x += 1
        else:
            self.x -= 1

    def get_current_color(self):
        return self.grid.get(self.x, dict()).get(self.y, 0)

if __name__ == '__main__':
    engine = IntcodeEngine('input', interactive=False)
    robot = DrawingRobot(engine)
    robot.run()
    print(robot.drawn_panels)
