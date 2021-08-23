class Telegram:
    def __init__(self, machine, time, step) -> None:
        self.machine = machine
        self.time = time
        self.step = step

    def alert_nurse(self): # When dry,wash,sterlize is completed
        print("Alert - Machine {0} is ready for collection.".format(self.machine))

    def alert_error(self): # When error occurs at any step
        print("Error - {0} is not complete at Machine {1}".format(self.step,self.machine))