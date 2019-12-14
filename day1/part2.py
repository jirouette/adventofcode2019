#!/usr/bin/python3
#coding: utf8
from math import floor

def compute_fuel(mass):
    if not mass:
        return 0
    fuel = floor(mass/3.0)-2
    if fuel < 0:
        fuel = 0
    return fuel + compute_fuel(fuel)

if __name__ == '__main__':
    total_fuel = 0
    with open('input') as f:
        for line in f:
            try:
                mass = int(line[:-1]) # without '\n'
                total_fuel += compute_fuel(mass)
            except ValueError:
                pass # empty line
    print(total_fuel)
