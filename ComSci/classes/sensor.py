import time

class Sensor:
    # step = dry / wash / sterlize
    # time = time required for step
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

    def start_cleaning(self,speed):
        if (speed == 'fast'): # For different wash cycle. Fast or normal
            self.wash()
            time.sleep(5)
            self.sterlize()
            time.sleep(5)
            self.dry()
            time.sleep(5)
        else:
            self.wash()
            time.sleep(10)
            self.sterlize()
            time.sleep(10)
            self.dry()
            time.sleep(10)

#For testing
testObject = Sensor("dry",10)
print(testObject.step)
print(testObject.time)