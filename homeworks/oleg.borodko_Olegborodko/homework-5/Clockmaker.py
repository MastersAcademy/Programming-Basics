class Clockmaker(object):
    def __init__(self, name="unknown", age=0, money=0):
        self.age = age
        self.name = name
        self.money = money
        print("Hello, my name is %s, and I have %s money" % (self.name, self.money))

    def clock_buy(self, clock):
        self.money -= clock.price
        print("Clock %s price is %s" % (type(clock).__name__, clock.price))
        print("I bought the %s" % type(clock).__name__)
        print("I have %s money now" % self.money)