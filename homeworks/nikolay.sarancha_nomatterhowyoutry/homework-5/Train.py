class Train:

	def __init__(self, color, maxSpeed, comfortLevel, ticketCost):
		self.color = color
		self.maxSpeed = maxSpeed
		self.comfortLevel = comfortLevel
		self.ticketCost = ticketCost

	def __str__(self):
		return "color: %s, maxSpeed: %i km/h, comfortLevel: %s class, ticketCost: %i $" % (self.color, self.maxSpeed, self.comfortLevel, self.ticketCost)