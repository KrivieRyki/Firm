from django.db import models


class Firm(models.Model):
    name = models.CharField(max_length=50)
    partner = models.ForeignKey('Firm', blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE, blank=True,)
    photo = models.ImageField()

    def __str__(self):
        return self.name
