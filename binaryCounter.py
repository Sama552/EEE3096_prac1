#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Sama Naraghi
Student Number: NRGSAM001
Prac: 1
Date: <21/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from itertools import product
import time

# public variables
binaryValues = list(product(range(2), repeat=3))
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Logic that you write
def main():
    countUp()
    refreshLEDs()
    time.sleep(1)

def countUp():
    global count
    if (count == 7):
        count = 0
    else:
        count = count + 1

def countDown():
    global count
    if (count == 0):
        count = 7
    else:
        count = count - 1

def refreshLEDs():
    global binaryValues
    global count
    print(binaryValues[count]);
    if (binaryValues[count][0] == 1):
        GPIO.output(17,GPIO.HIGH)
    else:
        GPIO.output(17,GPIO.LOW)
    if (binaryValues[count][1] == 1):
        GPIO.output(27,GPIO.HIGH)
    else:
        GPIO.output(27,GPIO.LOW)
    if (binaryValues[count][2] == 1):
        GPIO.output(22,GPIO.HIGH)
    else:
        GPIO.output(22,GPIO.LOW)


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while(True):
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)