from django.test import TestCase
from django.http import HttpRequest,HttpResponse
from unittest.mock import patch
from Employees.views import Employee_login
from django.contrib.auth import get_user_model,SESSION_KEY
from Employees.models import Employee
from unittest import skip
from django.contrib.auth.models import User
from Employees.views import Employee_page
from Companies.models import Company

class LoginViewsUnitTest(TestCase):

    def setUp(self):
        self.employee = Employee()
        self.employee.firstname='firstname'
        self.employee.lastname='lastname'
        self.employee.passwd = '123456'
        self.employee.save()

        self.arg = {'firstname':'firstname','lastname':'lastname','passwd':'123456'}
        self.username = self.arg['firstname']+self.arg['lastname']

        self.employee_user_model = User.objects.get(username = self.username)
    
    def test_login_renderer_correct_template(self):
        response = self.client.get('/employee/login')
        self.assertTemplateUsed(response,'login.html')

    @patch('Employees.views.authenticate')
    def test_login_calls_authenticate_during_post(self,mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/employee/login',self.arg)
        username = self.arg['firstname']+self.arg['lastname']
        password = self.arg['passwd']
        mock_authenticate.assert_called_once_with(username=username,password=password)

    
    def test_logged_in_session_if_authenticate_return_employee(
        self):

        self.client.post('/employee/login',self.arg)
        user_model = User.objects.get(username=self.username)
        self.assertEqual(self.client.session[SESSION_KEY],str(user_model.pk))


    @patch('Employees.views.authenticate')
    def test_does_not_log_in_session_if_authenticate_return_none(
        self,mock_authenticate):

        mock_authenticate.return_value = None
        self.client.post('/employee/login',self.arg)
        self.assertNotIn(SESSION_KEY,self.client.session)

    
    @patch('Employees.views.authenticate')
    @patch('Employees.views.redirect')
    def test_redirect_to_home_page_when_authenticate_fails(
        self,mock_redirect,mock_authenticate):

        mock_authenticate.return_value = None
        mock_redirect.return_value = HttpResponse()
        self.client.post('/employee/login',self.arg)
        mock_redirect.assert_called_once_with('home_page')

    
    @patch('Employees.views.authenticate')
    @patch('Employees.views.redirect')
    def test_redirect_to_employee_page_when_authenticate_return_a_user_model(
        self,mock_redirect,mock_authenticate):
        user = User.objects.get(username = self.username)
        user.backend = ''
        mock_authenticate.return_value = user
        mock_redirect.return_value = HttpResponse()
        self.client.post('/employee/login',self.arg)
        mock_redirect.assert_called_once_with('employee')

class EmployeeViewTest(TestCase):
    
    def setUp(self):
        self.employee = Employee()
        self.employee.firstname='firstname'
        self.employee.lastname='lastname'
        self.employee.passwd = '123456'
        self.employee.save()

        self.arg = {'firstname':'firstname','lastname':'lastname','passwd':'123456'}
        self.username = self.arg['firstname']+self.arg['lastname']

        self.employee_user_model = User.objects.get(username = self.username)

    def test_employee_view_uses_correct_template(self):
        self.client.post('/employee/login',data= self.arg)
        response = self.client.get('/employee/')
        self.assertTemplateUsed(response,'employe.html')

    def test_employee_view_uses_employee_model(self):
        self.client.post('/employee/login',data = self.arg)
        response = self.client.get('/employee/')
        self.assertEqual(self.employee,response.context['employe'])

    def test_company_feedback_view_renders_correct_html(self):
        company = Company.objects.create(name='Google',employe=self.employee)
        self.client.post('/employee/login',data= self.arg)
        response = self.client.get('/employee/company_feedback/Google/')
        self.assertTemplateUsed(response,'company_feedback.html')

    def test_company_feedback_view_uses_company_model(self):
        self.client.post('/employee/login',data= self.arg)
        company = Company.objects.create(name='Google',employe=self.employee)
        response = self.client.get('/employee/company_feedback/Google/')
        self.assertEqual(response.context['company'],company)
    
        
       

        
        
