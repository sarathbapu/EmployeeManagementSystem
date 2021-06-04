from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import EmployeeManager

ROLES = ((0, 'Admin'), (1, 'HR'), (2, 'Supervisor'), (3, 'General'))
GENDER = (('M', 'Male'), ('F', 'Female'), ('U', 'Unknown'), ('T', 'Transgender'))


class EmployeeModel(AbstractUser):

    username = None
    emp_id = models.BigIntegerField(verbose_name='Employee ID', unique=True, default=10000, auto_created=True)
    role = models.IntegerField(choices=ROLES, default=3)
    emp_phone = models.BigIntegerField(verbose_name='Phone Number')
    gender = models.CharField(choices=GENDER, default='U', max_length=2)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'emp_id'
    REQUIRED_FIELDS = []

    objects = EmployeeManager()

    def __str__(self):
        return f'User {self.last_name}, {self.first_name} : {self.emp_id}'

