#!/usr/bin/python3
#coding: utf8
from math import ceil, inf

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

def get_cross_positions(sequences):
    cross_positions = []
    positions = {}
    for sequence in sequences:
        posX = 0
        posY = 0
        for action in sequence:
            # First step : compute the vector (magnitude, direction)
            vectX = 0
            vectY = 0
            dirX = 0
            dirY = 0
            length = int(action[1:])
            direction = action[0]
            if direction == RIGHT:
                vectX = length
                dirX = 1
            elif direction == LEFT:
                vectX = -length
                dirX = -1
            elif direction == UP:
                vectY = length
                dirY = 1
            elif direction == DOWN:
                vectY = -length
                dirY = -1

            pathX = [posX] if dirX == 0 else range(posX+dirX, posX+vectX+dirX, dirX)
            pathY = [posY] if dirY == 0 else range(posY+dirY, posY+vectY+dirY, dirY)
            for x in pathX:
                for y in pathY:
                    # For each position : check if that position existed before
                    posX = x
                    posY = y
                    pos = (x, y)
                    if x in positions.keys():
                        if y in positions[x].keys():
                            cross_positions.append(pos)
                        else:
                            positions[x][y] = True
                    else:
                        positions[x] = {y: True}
    return cross_positions

def get_lowest_manhattan_distance(cross_positions):
    lowest_distance = inf
    for pos in cross_positions:
        distance = sum(abs(x) for x in pos)
        if distance < lowest_distance:
            lowest_distance = distance
    return lowest_distance

if __name__ == '__main__':
    sequences = []
    with open('input') as f:
        for line in f:
            sequences.append(line[:-1].split(','))
        cross_positions = get_cross_positions(sequences)
        print(get_lowest_manhattan_distance(cross_positions))
