from Page.login_page import Login
from Page.translator import Trans
class Page:
    def __init__(self,driver):
        self.driver = driver
    def get_login(self):
        return Login(self.driver)
    def get_trans(self):
        return Trans(self.driver)