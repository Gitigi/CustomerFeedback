from .base import FunctionalTest

class TestEmployees(FunctionalTest):

    def test_employees_can_login_and_view_their_assigned_company(self):

        self.browser.get(self.live_server_url)
        #An employe visit the site and notices there is a login
        #button on the top that allows employees to login
        #The employe click on the button
        self.browser.find_element_by_link_text('Login').click()

        #The employe is presented with a form to fill his
        #firstname ,lastname and password
        
        #The employe inputs the value and submit the form
        self.input_value_to_form('firstname','Mary')
        self.input_value_to_form('lastname','Wangui')
        self.input_value_to_form('passwd','12345')

        self.browser.find_element_by_id('submit').click()

        #after submittion the employe notices a logout button
        self.browser.find_element_by_link_text('Logout')
