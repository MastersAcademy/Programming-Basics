import time
from Clock import Clock

class SandClock(Clock):
    def __init__(self, size = "unknown", weight = "unknown", average_working_period = "unknown", count_time = "unknown"):
        self.count_time = int(count_time)

        Clock.__init__(self, size, weight, average_working_period)
        print("New Sand clock")

    def start(self):
        for i in range(self.count_time):
            time.sleep(1)
            print("clock")

        print("Now sand clock is empty, passed %s minutes" % self.count_time)