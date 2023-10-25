from django.db import models

class Player(models.Model):
    #List of choices for major value in database, human readable name
    LEVELS = (
        ('Advanced'),('Intermediate'),('N/A'),
    )
    TEAMNAME = (
        ('Name1'),('Name2'),('Name3'),('Name4'),('Name5'),('Name6'),('Name7'),('N/A'),
    )
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    teamLevel = models.CharField(max_length=200, choices=LEVELS, blank = True)
    teamName = models.CharField(max_length=200, choices=TEAMNAME, blank = True)
    phoneNum = models.CharField(max_length=200)

