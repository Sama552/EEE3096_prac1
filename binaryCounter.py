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
# import RPi.GPIO as GPIO
from itertools import product
import time

# public variables
binaryValues = list(product(range(2), repeat=3))
count = 0

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

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while(True):
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        # GPIO.cleanup()
    except e:
        # GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
