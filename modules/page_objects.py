from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    
    def __init__(self, driver):
       self.driver = driver
       self._url = "http://projectdreamteam.pythonanywhere.com/"
       self.navigate()

    def navigate(self):
        self.driver.get(self._url)
    
    @property
    def get_url(self):
        return self.driver.current_url

class NavBar(Base):
    
    def __init__(self, driver):
       Base.__init__(self,driver)
       self._login = self.driver.find_element_by_xpath("(//a[contains(@href, '/login')])[1]")
       self._register = self.driver.find_element_by_xpath("(//a[contains(@href, '/register')])[1]")
       self._home = self.driver.find_element_by_xpath("(//a[@href= '/'])[2]")
       
    def click_login(self):
        self._login.click()    

    @property
    def text_login(self):
        return self._login.text
    
    def click_register(self):
        self._register.click()    

    @property
    def text_register(self):
        return self._register.text

    def click_home(self):
        self._home.click()    

    @property
    def text_home(self):
        return self._home.text

class Home(NavBar):

    def __init__(self, driver):
       NavBar.__init__(self,driver)
       self._titulo = self.driver.find_element_by_xpath("//h1")
       self._subtitulo = self.driver.find_element_by_xpath("//h3")    

    @property
    def marca(self):
        return self._intro_msg.text

    @property
    def slogan(self):
        return self._registro.text

    

class Login(Base):
    def __init__(self, driver):
       Base.__init__(self, driver)
       self._url = 'http://projectdreamteam.pythonanywhere.com/login'
       self._email = "email" #ID
       self._password = "password" #ID
       self._submit = "submit" #ID
       self._message = "//div[contains(@class,'alert alert-info')]" #xpath
       self._login_name = "(//a)[4]" #path
    
    def login(self, user, password):
        self.driver.find_element_by_id(self._email).send_keys(user)
        self.driver.find_element_by_id(self._password).send_keys(password)
        self.driver.find_element_by_id(self._submit).click()
        
    @property
    def get_message_login_invalid(self):
        return self.driver.find_element_by_xpath(self._message).text

    @property
    def get_text_user_login(self):
        return self.driver.find_element_by_xpath(self._login_name).text

class Registro(Base):

    def __init__(self, driver):
       Base.__init__(self,driver)
       self._url = 'http://projectdreamteam.pythonanywhere.com/register'
       self._email = "email" #ID
       self._username = "username" #ID
       self._first_name = "first_name" #ID
       self._last_name = "last_name" #ID
       self._password = "password" #ID
       self.confirm_password = "confirm_password" #ID
       self._submit = "submit" #ID
       self._message = "(//p[contains(@class, 'help-block')])[1]" #xpath

    def register(self, email, username, first_name, last_name, password):
        self.driver.find_element_by_id(self._email).send_keys(email)
        self.driver.find_element_by_id(self._username).send_keys(username)
        self.driver.find_element_by_id(self._first_name).send_keys(first_name)
        self.driver.find_element_by_id(self._last_name).send_keys(last_name)
        self.driver.find_element_by_id(self._password).send_keys(password)
        self.driver.find_element_by_id(self.confirm_password).send_keys(password)
        self.driver.find_element_by_id(self._submit).click()

    @property
    def get_message_cadastro_invalid(self):
        return self.driver.find_element_by_xpath(self._message).text