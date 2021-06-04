from django.contrib.auth.base_user import BaseUserManager


class EmployeeManager(BaseUserManager):
    def create_user(self, emp_id, password, **other_fields):
        if not emp_id or emp_id == 0:
            raise ValueError('Employee ID should be a number')
        user = self.model(emp_id= emp_id, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, emp_id, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('role', 0)

        if other_fields.get('is_staff') is not True:
            raise ValueError('SuperUser should be a staff')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser flag should be true')
        if other_fields.get('role') != 0:
            raise ValueError('SuperUser should have admin role')

        return self.create_user(emp_id, password, **other_fields)
