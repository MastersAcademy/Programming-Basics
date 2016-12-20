from Terminator import Terminator

class T800(Terminator):
    def history(self):
        print('Formidable "cybernetic organism", robotic assassin and soldier, designed by the military supercomputer \n'
              'Skynet for infiltration and combat duty, towards the ultimate goal of exterminating the human resistance.')

class T850(Terminator):
    __life = '200 years'
    def history(self):
        print('An enhanced version of the T-800, which uses a different power source: two overlapping hydrogen fuel \n'
              'cell with the ability to access and replace for 200 years. Also simplified the procedure for removal of\n'
              'human flesh with the endoskeleton and the ability to restart the operating system, control the terminator.')

bad_robot = T800('T800', 'mini reactor', 'different handguns', 'organic camouflage')
arnold = T850('T850', 'mini reactor', 'different handguns', 'organic camouflage')

print("model: %s, power_source: %s, firearms: %s, skin: %s" % (bad_robot.model, bad_robot.power_source, bad_robot.firearms, bad_robot.skin))
bad_robot.history()

print('-====____________________****___________________====-')

print("model: %s, power_source: %s, firearms: %s, skin: %s" % (arnold.model, arnold.power_source, arnold.firearms, arnold.skin))
arnold.history()

# print(arnold.__life) # encapsulation test
