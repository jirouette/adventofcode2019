#!/usr/bin/python3
#coding: utf8

DOUBLES = [str(x)*2 for x in range(0, 10)]

def guess_nb_possible_passwords(MIN, MAX):
	nb = 0
	for n in range(MIN, MAX+1):
		n = str(n)
		for double in DOUBLES:
			if double in n:
				break
		else:
			continue # no double digit, abort
		lowest = 0
		for i in n:
			i = int(i)
			if i < lowest:
				break
			lowest = i
		else:
			nb += 1
	return nb

if __name__ == '__main__':
	MIN = 264360
	MAX = 746325
	print(guess_nb_possible_passwords(MIN, MAX))
