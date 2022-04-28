from gripper_motor import *
from wrist_motor import *
from upper_arm import *
from lower_arm import *
from waist import *

import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711


referenceUnit = 1



def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(31,29)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(343690/720.3)
hx.reset()
hx.tare()


while True:
    val = hx.get_weight(5)
    print(val)
#     if val >=75:
#         homing
#         homing(waist)
#         break
    hx.power_down()
    hx.power_up()
    time.sleep(0.1)

