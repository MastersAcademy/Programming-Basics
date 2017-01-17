from Car import Car

class Truck(Car):
	def __init__(self, count_wheels, engine, body, max_weight):
		Car.__init__(self, count_wheels, engine, body)
		self.max_weight = max_weight

	def load_weight(self, weight):
		self.weight = weight
		if weight < max_weight:
			return "load complete"
		else:
			return "max_weight exceeded"

	def drive(self):
		return 'drive with speed 50 km'




