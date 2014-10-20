import time
import logging
import serial
import lib.execute

import lib.handlers.handlerTemplates as handlerTemplates


class TripodActuatorHandler(handlerTemplates.ActuatorHandler):
    def __init__(self, executor, comPort, shared_data):
        """
        The init handler of Tripod

        comPort (string): The comport to connect to (default="/dev/ttyUSB0")
        """

        self.tripodSer = None   #serial port for tripod
        #Defaults
        self.baud = 9600     #set baud rate
        self.timeout = 0.5     #in seconds

        try:
            self.tripodSer = serial.Serial(port = comPort, baudrate =
                                           self.baud, timeout = self.timeout)

            # set robot to neutral position
            self.tripodSer.write("o")
            self.tripodSer.flush()
        except:
            logging.exception("Couldn't connect to Tripod")
            exit(-1)

    def grip(self, actuatorVal, initial=False):
        """
        tells robot to go grip/release
        """
        if initial:
            return
        if actuatorVal:
            self.tripodSer.write("c")
            self.tripodSer.flush()

    def openGrip(self, actuatorVal, initial=False):
        """
        tells robot to go grip/release
        """
        if initial:
            return
        if actuatorVal:
            self.tripodSer.write("o")
            self.tripodSer.flush()

if __name__ == "__main__":
    executor = lib.execute.LTLMoPExecutor()
    h = TripodActuatorHandler(executor, "/dev/ttyUSB0")
    while True:
        s = raw_input("Please type your command: ")
        if s == "c":
            h.grip(True)
        else:
            h.openGrip(False)

