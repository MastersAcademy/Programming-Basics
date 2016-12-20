from Train import Train


class touristicTrain(Train):

	def __init__(self, color, maxSpeed, comfortLevel, ticketCost):
		super(Imagination, self).__init__(color, maxSpeed, comfortLevel, ticketCost)

	def __str__(self):
		return "color: %s, maxSpeed: %i km/h, comfortLevel: %s class, ticketCost: %i $" % (self.color, self.maxSpeed, self.comfortLevel, self.ticketCost)

	def exciting(self):
		print 'Wow, dude! What a view.'

	exciting(Imagination)
