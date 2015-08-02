from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from Customer.models import Company

class CustomerTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_customer_is_presented_with_a_list_of_company(self):
        #A customer visits the feedback site to give his
        #feedback on a particula company
        
        ##Create a list of companies
        company1 = Company()
        company1.name = 'Google'
        company1.save()
        company2 = Company()
        company2.name = 'Cnn'
        company2.save()
        
        self.browser.get(self.live_server_url)

        #when to webpage loads, the customer sees a a table
        #which is populate with a list of company
        self.assertIn('Google',self.browser.find_element_by_tag_name('table').text)
        self.assertIn('Cnn',self.browser.find_element_by_tag_name('table').text)

        
