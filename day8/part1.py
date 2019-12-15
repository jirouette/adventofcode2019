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
		layers = [line[i*LAYER:(i+1)*LAYER] for i in range(int(length/LAYER))]
		target_layer = layers[0]
		fewest_nb_zero = inf
		for layer in layers:
			nb_zero = layer.count('0')
			if nb_zero < fewest_nb_zero:
				fewest_nb_zero = nb_zero
				target_layer = layer
		print(target_layer.count('1')*target_layer.count('2'))
