from Page.login_page import Login

class Page:
    def __init__(self,driver):
        self.driver = driver
    def get_login(self):
        return Login(self.driver)