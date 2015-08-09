from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from Companies.models import Company

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def create_a_company_in_database(self,name,logo='',description=''):
        comp = Company()
        comp.name = name
        comp.logo = logo
        comp.description=description
        comp.save()

    def input_value_to_form(self,input_id,value):
        self.browser.find_element_by_id(input_id).send_keys(value)
