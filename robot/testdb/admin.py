from django.contrib import admin
from .models import Robot, RobotEvent

# Register your models here.
admin.site.register(Robot)
admin.site.register(RobotEvent)
