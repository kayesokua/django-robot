from django.db import models
ACTIONDESC = ((0, "Test"), (1, "Grab the Glass"))

class Robot(models.Model):
    name = models.CharField(max_length=80)
    dof = models.IntegerField(default=0)
    desc_construction = models.TextField(default="Replace the text here")
    desc_hardware = models.TextField(default="Replace the text here")
    img = models.ImageField(upload_to="media/robot",default="empty.jpg")
    img_circuit = models.ImageField(upload_to="media/circuit_img",default="empty.jpg")
    url_cad_files = models.URLField(blank="True",default="https://www.thingiverse.com/")
    

    def __str__(self):
        return self.name

class RobotEvent(models.Model):
    robot_name = models.ForeignKey(Robot, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    dof_1 = models.IntegerField(blank=True,default=0)
    dof_2 = models.IntegerField(blank=True,default=0)
    dof_3 = models.IntegerField(blank=True,default=0)
    dof_4 = models.IntegerField(blank=True,default=0)
    dof_5 = models.IntegerField(blank=True,default=0)
    dof_6 = models.IntegerField(blank=True,default=0)
    action = models.IntegerField(choices=ACTIONDESC, default=0)

    def __str__(self):
        return f"{self.robot_name} {self.created_on}"