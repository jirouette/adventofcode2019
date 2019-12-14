#!/usr/bin/python3
#coding: utf8

PATTERNS = [(str(x)*2,str(x)*3) for x in range(0, 10)]

def guess_nb_possible_passwords(MIN, MAX):
	nb = 0
	for n in range(MIN, MAX+1):
		n = str(n)
		for pattern in PATTERNS:
			if pattern[0] in n and pattern[1] not in n:
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
