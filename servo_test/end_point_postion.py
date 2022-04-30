from cmath import acos, atan, sqrt
# from gripper_motor import *
# from wrist_motor import *
# from upper_arm import *
# from lower_arm import *
# from waist_motor import *

X = 10.0 # desired X position of end-effector
Y = 0.0 # desired X position of end-effector
Z = 5.0 # desired X position of end-effector
a1= 16 #cm
a2= 11.4 #cm
a3= 14.8 #cm


r2 = sqrt(X*X+Y*Y) # equation 1

T1 = acos(((r2*r2)+(X*X)-(Y*Y))/(2*r2*X)) #equation 2

r1 = sqrt((Z-a1)*(Z-a1)+(r2*r2)) #equation 3

phi1 = atan((Z-a1)/r2) #equation 4

phi2 = acos(((a2*a2)+(r1*r1)-(a3*a3))/(2*a2*r1)) #equation 5

T2 = phi1+phi2 #radians #equation 6

phi3 = acos(((a3*a3)+(r1*r1)-(a2*a2))/(2*a3*r1)) #equation 7

T3 = phi2-phi3 #radians #equation 8

upper_arm = T3/3.14159*180.0
lower_arm = T2/3.14159*180.0
waist = T1/3.14159*180

print("Theta 1: ", waist, ". Theta 2: ", lower_arm, "Theta 3: ", upper_arm)









