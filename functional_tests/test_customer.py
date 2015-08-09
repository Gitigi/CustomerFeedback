from selenium import webdriver
from .base import FunctionalTest

class CustomerTest(FunctionalTest):

    def test_customer_is_presented_with_a_list_of_company(self):
        #A customer visits the feedback site to give his
        #feedback on a particula company
        
        ##Create a list of companies
        self.create_a_company_in_database('Google','google.jpg')
        self.create_a_company_in_database('Cnn','cnn.png')
        
        self.browser.get(self.live_server_url)

        #when to webpage loads, the customer sees a a table
        #which is populate with a list of company
        self.assertIn('Google',self.browser.find_element_by_tag_name('table').text)
        self.assertIn('Cnn',self.browser.find_element_by_tag_name('table').text)


    def test_customer_can_select_a_company_and_be_presented_with_a_form(self):
        #once the homepage has loaded the customer sees a company that he wanted
        #to post a feedback
        #He click on the row whick containst the company details
        self.create_a_company_in_database('Google','google.jpg')
        
        self.browser.get(self.live_server_url)
        homepage_url = self.browser.current_url
        
        self.browser.find_element_by_id('Google').click()

        form = self.browser.find_element_by_tag_name('form').text
        #The form contains input for First Name, Last Name, Phone No,
        #and Feedback
        self.assertIn('First Name',form)
        self.assertIn('Last Name',form)
        self.assertIn('Phone No.',form)
        self.assertIn('Feedback',form)

        #The Customer inputs value into the form
        #and submits it
        self.input_value_to_form('firstname','Stephen')
        self.input_value_to_form('lastname','Gitigi')
        self.input_value_to_form('phone_no','334343434')
        self.input_value_to_form('feedback','What a greate service you offer')
        self.browser.find_element_by_id('submit').click()

        #The customer notices that the page return to the home page with a lis
        #of registered company
        self.assertTrue(homepage_url,self.browser.current_url)
        self.assertIn('Google',self.browser.find_element_by_tag_name('table').text)

        

    
