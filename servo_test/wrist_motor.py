from helper_functions import *
import RPi.GPIO as GPIO
import time

def pour(motor) :
    pos = 100
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
def homing(motor):
    pos = 0
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
wrist = motor_setup(11)
homing(wrist)
pour(wrist)
homing(wrist)