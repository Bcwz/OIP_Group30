
class Sensor:
    def __init__(self, step, time) -> None:
        self.step = step
        self.time = time
        
    def wash(self):
        #Insert command to start washing here
        print("Machine is {0} for {1} mins.".format(self.step,self.time))

    def dry(self):
        #Insert command to start drying here
        print("Machine is {0} for {1} mins.".format(self.step,self.time))

    def sterlize(self):
        #Insert command to start sterilzing here
        print("Machine is {0} for {1} mins.".format(self.step,self.time))

#For testing
testObject = Sensor("dry",10)
print(testObject.step)
print(testObject.time)