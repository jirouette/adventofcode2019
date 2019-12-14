#!/usr/bin/python3
#coding: utf8
from math import floor

if __name__ == '__main__':
    fuel = 0
    with open('input') as f:
        for line in f:
            try:
                mass = int(line[:-1]) # without '\n'
                fuel += floor(mass/3.0)-2
            except ValueError:
                pass # empty line
    print(fuel)
