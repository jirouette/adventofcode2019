#!/usr/bin/python3
#coding: utf8
from math import inf

WIDTH = 25
HEIGHT = 6
LAYER = WIDTH*HEIGHT

if __name__ == '__main__':
	with open('input') as f:
		line = f.readline()
		length = int(len(line))
		layers = [[line[i*LAYER:(i+1)*LAYER][j*WIDTH:(j+1)*WIDTH] for j in range(HEIGHT)] for i in range(int(length/LAYER))]
		for y in range(len(layers[0])):
			for x in range(len(layers[0][y])):
				layer = 0
				px = "2"
				while px == "2":
					px = layers[layer][y][x]
					layer += 1
				print(px.replace('0', ' '), end="")
			print()