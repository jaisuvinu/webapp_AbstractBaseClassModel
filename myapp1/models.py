from django.db import models

# Abstract base class:
class Employee(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    class Meta:
        abstract=True

# Derived class:
class RegularEmployee(Employee):
    salary=models.IntegerField()
    bonus=models.IntegerField()
    def __str__(self):
        return self.name

# Derived class:
class ContractEmployee(Employee):
    payperhour=models.IntegerField()
    duration=models.IntegerField()
    def __str__(self):
        return self.name
