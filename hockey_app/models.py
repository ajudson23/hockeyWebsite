from django.db import models

class Player(models.Model):
    LEVELS = [
        ('Advanced', 'Advanced'),
        ('Intermediate', 'Intermediate'),
        ('N/A', 'N/A'),
    ]
    TEAMNAME = [
        ('Name1', 'Name1'),
        ('Name2', 'Name2'),
        ('Name3', 'Name3'),
        ('Name4', 'Name4'),
        ('Name5', 'Name5'),
        ('Name6', 'Name6'),
        ('Name7', 'Name7'),
        ('N/A', 'N/A'),
    ]
    firstName = models.CharField("First Name", max_length=200)
    lastName = models.CharField("Last Name", max_length=200)
    email = models.CharField("Email", max_length=200)
    teamLevel = models.CharField("Team Level", max_length=200, choices=LEVELS, blank=False)
    teamName = models.CharField("Team Name", max_length=200, choices=TEAMNAME, blank=False)
    phoneNum = models.CharField("Phone Number", max_length=200)
