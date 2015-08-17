from .base import FunctionalTest

class TestEmployees(FunctionalTest):

    def test_employees_can_login_logout_and_view_their_assigned_company(self):

        self.browser.get(self.live_server_url)
        #An employe visit the site and notices there is a login
        #button on the top that allows employees to login
        #The employe click on the button
        homepage_url = self.browser.current_url
        self.browser.find_element_by_link_text('Login').click()

        #The employe is presented with a form to fill his
        #firstname ,lastname and password

        ##Create an employee in database
        employee = self.create_an_employee_in_database('Mary','Trasy','12345')
        ##Create a Company in database
        self.create_a_company_in_database(name = 'Google',employe = employee)
        self.create_a_company_in_database(name = 'Cnn')
        
        #The employe inputs the value and submit the form
        self.input_value_to_form('firstname','Mary')
        self.input_value_to_form('lastname','Trasy')
        self.input_value_to_form('passwd','12345')

        self.browser.find_element_by_id('submit').click()

        #After submiting the form, the Employe notices she is loged in as Trasy
        navigation = self.browser.find_element_by_tag_name('nav')
        self.assertIn('Trasy',navigation.text)

        #The employe is presented with a list of companies that she
        #is assigned
        self.assertIn('Google',self.browser.find_element_by_tag_name('table').text)
        self.assertNotIn('Cnn',self.browser.find_element_by_tag_name('table').text)

        #when the Employee logout, he notices that the page redirects to homepage
        self.browser.find_element_by_link_text('Logout').click()
        self.assertEqual(self.browser.current_url,homepage_url)

    def test_employee_can_select_a_company_see_all_the_feedback_and_reply_to_them(
        self):

        employee = self.create_an_employee_in_database('Mary','Trasy','12345')
        company  = self.create_a_company_in_database(name = 'Apple',employe = employee)
        feed = self.create_a_feedback_in_database(firstname='Jane',feedback='Great job',
                                                  company = company)

        self.login_employee('Mary','Trasy','12345')
        self.browser.find_element_by_id(company.name).click()
        self.assertIn(feed.feedback,self.browser.find_element_by_tag_name('body').text)

        
        




        
