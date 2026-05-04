from django.db import models

# Create your models here.
class employees(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    emp_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name