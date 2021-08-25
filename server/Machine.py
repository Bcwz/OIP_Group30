from debug import log
import Constants
import sys
import adafruit_dht
import random


class Machine:
    # step = dry / wash / sterlize
    # time = time required for step
    def __init__(self) -> None:
        log("init machine")
        self.state = Constants.IDLE
        self.speed = Constants.SPEED_NORMAL

    def get_humidity(self) -> str:
        return str(random.randint(0,100))

    def get_temperature(self) -> str:
        return str(random.randint(0,100))

    def wash(self) -> None:
        # Insert command to start washing here
        log("wash", "Machine is {0} for {1} mins.".format(
            self.step, self.time))

        self.state = Constants.WASHING

    def dry(self) -> None:
        # Insert command to start drying here
        log("dry", "Machine is {0} for {1} mins.".format(self.step, self.time))

        self.state = Constants.DRYING

    def sterilize(self) -> None:
        # Insert command to start sterilzing here
        log("sterilize", "Machine is {0} for {1} mins.".format(
            self.step, self.time))

        self.state = Constants.STERILIZING

    def start_cleaning(self) -> None:
        log("start_cleaning")
        self.wash()
        self.sterilize()
        self.dry()
