#!/usr/bin/env python3

class Vehicle(object):

	def __init__(self, model, color):
		self.model = model
		self.color = color

	def car_info(self):
		return "\nVehicle:\nModel: \'%s\', Color: \'%s\'" % (self.model, self.color)

	