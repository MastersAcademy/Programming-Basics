import time
import random
from Clock import Clock

class Sundial(Clock):
    def __init__(self, size = "unknown", weight = "unknown", average_working_period = "unknown"):
        Clock.__init__(self, size, weight, average_working_period)
        print("New Sundial clock")

    def show_time(self):
        error_calculations = random.randint(1, int(time.strftime("%M")))
        hours_now = int(time.strftime("%H"))

        if hours_now <= 18:
            print("Time now approximately - %s : %s" % (hours_now, error_calculations))
        else:
            print("Clock not working (sky is dark)")