from django.db import models

class EmployeeModel(models.Model):

    name = models.CharField('Name', max_length=50, null=True)
    age = models.IntegerField('Age', default=18)
    password = models.CharField('Password', max_length=50)


    def __str__(self):
        return self.name