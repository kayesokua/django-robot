# Generated by Django 4.0.4 on 2022-04-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0002_robot_img_robotevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robotevent',
            name='dof_1',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='robotevent',
            name='dof_2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='robotevent',
            name='dof_3',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='robotevent',
            name='dof_4',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='robotevent',
            name='dof_5',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='robotevent',
            name='dof_6',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
