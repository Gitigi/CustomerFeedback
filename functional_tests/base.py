from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from Companies.models import Company,Feedback
from Employees.models import Employee
from django.contrib.auth import SESSION_KEY,BACKEND_SESSION_KEY,authenticate
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.models import User
from django.conf import settings


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def create_a_company_in_database(self,name,logo='',description='',employe=None):
        comp = Company()
        comp.name = name
        comp.logo = logo
        comp.description=description
        comp.employe = employe
        comp.save()
        return comp

    def create_an_employee_in_database(self,firstname,lastname,password):
        employee = Employee()
        employee.firstname = firstname
        employee.lastname = lastname
        employee.passwd = password
        employee.save()
        return employee

    def create_a_feedback_in_database(self,firstname,lastname='',phone_no='',
                                      feedback = '' ,company=None):

        feed = Feedback()
        feed.firstname = firstname
        feed.lastname = lastname
        feed.phone_no = phone_no
        feed.feedback = feedback
        feed.company = company
        feed.save()
        return feed

    def login_employee(self,firstname,lastname,password):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Login').click()
        
        self.input_value_to_form('firstname',firstname)
        self.input_value_to_form('lastname',lastname)
        self.input_value_to_form('passwd',password)

        self.browser.find_element_by_id('submit').click()
        

    def input_value_to_form(self,input_id,value):
        self.browser.find_element_by_id(input_id).send_keys(value)
