import py_compile
from django.shortcuts import render        
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Robot
from .sensors.servos import *
from .sensors.camera import *


def start(request):    
    #if label is detected by camera is 'raki' and weight is '40g'
    #then start grabing the botll from location
    return HttpResponse('<h1>Start the script of the Robot</h1>')

def robot_profile(request, robot_id):
    robot = get_object_or_404(Robot, pk=robot_id)
    print(robot.name,robot.dof,robot.img)
    return render(request, 'robot_page.html', {'robot':robot})

def test_robot_arm(request):
    return HttpResponse('<h1>Testing the range of movements of the robotic arm</h1>')
