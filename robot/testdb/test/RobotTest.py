from django.test import TestCase
from models import Robot, RobotEvent

class RobotTestCase(TestCase):
    def setUp(self):
        Robot.objects.create(
            name="Mida's Hand",
            dof=6,
            desc_construction = "Additive fabrication using 3D Printer",
            desc_hardware = "I am powered by Rpi4",
            img = "picture.png",
            img_circuit = "circuit.png",
            url_cad_files = "https://www.thingiverse.com/")

class RobotEvent(TestCase):
    def setUp(self):
        RobotEvent.objects.create(
            robot_name = "Plywood Prototype",
            created_on = "2022-04-16",
            dof_1 = 45,
            dof_2 = 90,
            dof_3 = 45,
            dof_4 = 90,
            dof_5 = 90,
            dof_6 = 0,
            action = 1)