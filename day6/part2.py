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

	def get_nb_of_orbits(self, until=None):
		return len(self.get_full_parent_list(until))

	def get_full_parent_list(self, until=None):
		parent = self.parent
		parent_list = []
		if until is not None:
			until = OrbitalObject.objects.get(until)
		while parent is not until and parent is not None:
			parent_list.append(parent)
			parent = parent.parent
		return parent_list

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
		YOU = OrbitalObject.objects.get('YOU')
		SAN = OrbitalObject.objects.get('SAN')
		YOU_parents = YOU.get_full_parent_list()
		SAN_parents = SAN.get_full_parent_list()
		closest_parent_name = None
		for parent in YOU_parents:
			if parent in SAN_parents:
				closest_parent_name = parent.name
				break
		print('From YOU to',closest_parent_name,':',YOU.get_nb_of_orbits(closest_parent_name))
		print('From SAN to',closest_parent_name,':',SAN.get_nb_of_orbits(closest_parent_name))
		print("Lowest required orbital transfers :",YOU.get_nb_of_orbits(closest_parent_name)+SAN.get_nb_of_orbits(closest_parent_name))