from django.contrib.auth import get_user_model
Employee = get_user_model()

class EmployeeAuthenticationBackend(object):

    def authenticate(self,employee_details):
        try:
            employee = Employee.objects.get(lastname=employee_details['lastname'])
            if employee.passwd == employee_details['passwd']:
                return employee
            else:
                return None
        except Employee.DoesNotExist:
            return None

    def get_employee(self,lastname):
        try:
            return Employee.objects.get(lastname=lastname)
        except Employee.DoesNotExist:
            return None
