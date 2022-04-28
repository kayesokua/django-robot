import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
servoPin=26

#position 9 = wrist facing front
#position 9 start should be 2
Positions = [1,2,3,4,5,6,7,8,9,10,11,12]

GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(0)

for angle in range(1,180):
    dc=1./18.* (float(angle)) + 2
    pwm.ChangeDutyCycle(dc)
    print("position:",angle)
    print("DC:",dc)
    time.sleep(0.015)

print("reverseeeeee")
print("reverseeeeee")
print("reverseeeeee")

time.sleep(3)

for angle2 in range(90,2,-1):
    dc=1./18.* (float(angle2)) + 2
    pwm.ChangeDutyCycle(dc)
    print("position:",angle)
    print("DC:",dc)
    time.sleep(0.015)

pwm.stop()
GPIO.cleanup()