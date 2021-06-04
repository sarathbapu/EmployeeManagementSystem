from django.db import models

from Employee.models import EmployeeModel

STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Rejected'))


class LeaveModel(models.Model):
    leave_id = models.IntegerField(auto_created=True, default=1, primary_key=True)
    applied_by = models.ForeignKey(EmployeeModel, blank=False, on_delete=models.CASCADE, related_name='Employee')
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    acted_by = models.ForeignKey(EmployeeModel, blank=True, on_delete=models.CASCADE, related_name='Supervisor')
    acted_on = models.DateTimeField()

    def __str__(self):
        return f'Leave request {self.leave_id} by {self.applied_by}'