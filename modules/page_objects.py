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
    def text_regiter(self):
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

    

class Login(NavBar):

    def __init__(self, driver):
       NavBar.__init__(self,driver)
       

