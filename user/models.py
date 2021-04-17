from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    mid_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    date_of_birth = models.DateField(blank=True, null=True)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.mid_name + ' ' + self.last_name