#!/usr/bin/python3
#coding: utf8

class OrbitalObject:
	def __init__(self, orbitting, name):
		self.name = name
		self.parent = None
		self.children = []
		OrbitalObject.objects[name] = self
		if orbitting is not None:
			self.set_orbitting(orbitting)

	def set_orbitting(self, orbitting):
		parent = OrbitalObject.objects.get(orbitting)
		if not parent:
			parent = OrbitalObject(None, orbitting)
		parent.children.append(self)
		self.parent = parent

	def get_nb_of_orbits(self):
		parent = self.parent
		nb = 0
		while parent is not None:
			nb += 1
			parent = parent.parent
		return nb

OrbitalObject.objects = dict()

if __name__ == '__main__':
	with open('input') as f:
		for line in f:
			orbitting, name = line[:-1].split(")")
			obj = OrbitalObject.objects.get(name)
			if obj:
				obj.set_orbitting(orbitting)
			else:
				OrbitalObject(orbitting, name)
	print(sum([obj.get_nb_of_orbits() for obj in OrbitalObject.objects.values()]))
