from helper_functions import *
import RPi.GPIO as GPIO
import time

def homing(motor):
    pos = 90
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
def lower(motor):
    pos = 120
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
upper_arm = motor_setup(15)
# homing(upper_arm)                        
# lower(upper_arm)
# homing(upper_arm)

clean_up(upper_arm)