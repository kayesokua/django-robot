# Write your code here :-)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin = 35

GPIO.setup(pin, GPIO.OUT)
motor1 = GPIO.PWM(pin, 50)
motor1.start(0)



#motor1.ChangeDutyCycle(9.5)
#time.sleep(0.5)
# 
# angle = 0
# dc = 1/18*(angle)+2
# 
# motor1.ChangeDutyCycle(dc)
# time.sleep(0.2)
# motor1.ChangeDutyCycle(0)
# time.sleep(1)


# 
for degree in range(0,181,10):
    dc = 1/18*(degree)+2
    motor1.ChangeDutyCycle(dc)
    time.sleep(0.2)
    motor1.ChangeDutyCycle(0)
    print("the degree turns to: ",degree)
    time.sleep(0.5)

for degree in range(180,-1,-10):
    dc = 1/18*(degree)+2
    motor1.ChangeDutyCycle(dc)
    time.sleep(0.2)
    motor1.ChangeDutyCycle(0)
    print("the degree turns to: ",degree)
    time.sleep(0.5)
    




motor1.stop()
# motor2.stop()
GPIO.cleanup()