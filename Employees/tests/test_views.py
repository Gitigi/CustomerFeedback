from django.test import TestCase
from django.http import HttpRequest,HttpResponse
from unittest.mock import patch
from Employees.views import Employee_login
from django.contrib.auth import get_user_model,SESSION_KEY
from Employees.models import Employee
from unittest import skip
User = get_user_model()

class LoginViewsUnitTest(TestCase):

    def setUp(self):
        self.employee = Employee()
        self.employee.firstname='firstname'
        self.employee.lastname='lastname'
        self.employee.passwd = '123456'
        self.employee.save()

        self.arg = {'firstname':'firstname','lastname':'lastname','passwd':'123456'}
        self.username = self.arg['firstname']+self.arg['lastname']
    
    def test_login_renderer_correct_template(self):
        response = self.client.get('/login')
        self.assertTemplateUsed(response,'login.html')

    @patch('Employees.views.authenticate')
    def test_login_calls_authenticate_during_post(self,mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/login',self.arg)
        username = self.arg['firstname']+self.arg['lastname']
        password = self.arg['passwd']
        mock_authenticate.assert_called_once_with(username=username,password=password)

    
    def test_logged_in_session_if_authenticate_return_employee(
        self):

        self.client.post('/login',self.arg)
        user_model = User.objects.get(username=self.username)
        self.assertEqual(self.client.session[SESSION_KEY],str(user_model.pk))


    @patch('Employees.views.authenticate')
    def test_does_not_log_in_session_if_authenticate_return_none(
        self,mock_authenticate):

        mock_authenticate.return_value = None
        self.client.post('/login',self.arg)
        self.assertNotIn(SESSION_KEY,self.client.session)

    
    @patch('Employees.views.authenticate')
    @patch('Employees.views.redirect')
    def test_redirect_to_home_page_when_authenticate_fails(
        self,mock_redirect,mock_authenticate):

        mock_authenticate.return_value = None
        mock_redirect.return_value = HttpResponse()
        self.client.post('/login',self.arg)
        mock_redirect.assert_called_once_with('home_page')

    
    @patch('Employees.views.authenticate')
    @patch('Employees.views.redirect')
    def test_redirect_to_employee_page_when_authenticate_return_a_user_model(
        self,mock_redirect,mock_authenticate):
        user = User.objects.get(username = self.username)
        user.backend = ''
        mock_authenticate.return_value = user
        mock_redirect.return_value = HttpResponse()
        self.client.post('/login',self.arg)
        mock_redirect.assert_called_once_with('employee')

    def test_employee_renders_right_template(self):
        response = self.client.post('/employee/')
        self.assertTemplateUsed(response,'employe.html')

    
        

        
        
