from helper_functions import *
import RPi.GPIO as GPIO
import time

def homing(motor):
    pos = 90
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
def turn(motor, degree):
    dc = degree_to_DC(degree)
    change_DC(motor,dc)
    
upper_arm = motor_setup(15)
# homing(upper_arm)                        
# lower(upper_arm)
# homing(upper_arm)

clean_up(upper_arm)