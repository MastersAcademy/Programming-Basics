from Train import Train


class speedTrain(Train):

	def __init__(self, color, maxSpeed, comfortLevel, ticketCost):
		super(Comet, self).__init__(color, maxSpeed, comfortLevel, ticketCost)

	def __str__(self):
		return "color: %s, maxSpeed: %i km/h, comfortLevel: %s class, ticketCost: %i $" % (self.color, self.maxSpeed, self.comfortLevel, self.ticketCost)

	def tooFast(self):
		print 'One of the passengers just puked, keep raising speed!'

	tooFast(Comet)