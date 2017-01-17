class Car(object):
	def __init__(self, count_wheels, engine, body):
		self.count_wheels = count_wheels
		self.engine = engine
		self.body = body

	def start_engine(self):
		return 'Engine started!!'

	def stop_engine(self):
		return 'Engine stopped'

	def drive(self):
		return 'drive with speed 70 km'
