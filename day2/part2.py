#!/usr/bin/python3
#coding: utf8
from math import ceil

HALT = 99
ADD = 1
MUL = 2

def intcodes(noun, verb):
    sequence = []
    with open('input') as f:
        sequence = [int(x) for x in f.readline().split(',')]
        sequence[1] = noun
        sequence[2] = verb
        for operation_pos in range(ceil(len(sequence)/4)):
            chunk = sequence[operation_pos*4:operation_pos*4+4]
            operation = chunk[0]
            if operation == HALT:
                break
            pos1 = chunk[1]
            pos2 = chunk[2]
            pos_result = chunk[3]
            if operation == ADD:
                sequence[pos_result] = sequence[pos1] + sequence[pos2]
            elif operation == MUL:
                sequence[pos_result] = sequence[pos1] * sequence[pos2]
    return sequence

if __name__ == '__main__':
    OUTPUT = 19690720
    for noun in range(100):
        for verb in range(100):
            sequence = intcodes(noun, verb)
            if sequence[0] == OUTPUT:
                print("Noun = ", noun)
                print("Verb = ", verb)
                print("Result = ", 100*noun+verb)
                break
        else:
            continue
        break
