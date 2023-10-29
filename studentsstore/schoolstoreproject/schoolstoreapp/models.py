# models.py

from django.db import models

DEPARTMENT_CHOICES = [
    ('Computer Science', 'Computer Science'),
    ('Commerce', 'Commerce'),
    # Add more departments
]

class Registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # Add other user fields
    def __str__(self):
        return self.username


