#!/usr/bin/python3
#coding: utf8
from math import ceil

HALT = 99
ADD = 1
MUL = 2

if __name__ == '__main__':
    sequence = []
    with open('input') as f:
        sequence = [int(x) for x in f.readline().split(',')]
        sequence[1] = 12 # as required
        sequence[2] = 2 # as required
        for operation_pos in range(ceil(len(sequence)/4)):
            chunk = sequence[operation_pos*4:operation_pos*4+4]
            print(chunk)
            operation = chunk[0]
            if operation == HALT:
                print("HALT")
                break
            pos1 = chunk[1]
            pos2 = chunk[2]
            pos_result = chunk[3]
            if operation == ADD:
                sequence[pos_result] = sequence[pos1] + sequence[pos2]
            elif operation == MUL:
                sequence[pos_result] = sequence[pos1] * sequence[pos2]
            print(sequence)
    print(sequence)
