#!/usr/bin/python3
#coding: utf8
from math import ceil, inf

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

def get_cross_positions(sequences):
    cross_positions = {}
    positions = []
    for sequence in sequences+[sequences[0]]:
        current_positions = {}
        cross_steps = {}
        posX = 0
        posY = 0
        steps = 0
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
                    steps += 1
                    # For each position : check if that position existed before
                    posX = x
                    posY = y
                    pos = (x, y)
                    for prev_position in positions[-1:]:
                        if x in prev_position.keys():
                            if y in prev_position[x].keys():
                                if pos not in cross_steps.keys():
                                    cross_steps[pos] = steps
                                    cross_positions[pos] = cross_positions.get(pos, 0) + steps
                    if x not in current_positions.keys():
                        current_positions[x] = {}                    
                    current_positions[x][y] = True
        positions.append(current_positions)
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
        print(min(cross_positions.values()))
