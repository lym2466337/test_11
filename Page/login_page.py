from selenium.webdriver.common.by import By

from Base.Base_Action import BaseAction


class Login(BaseAction):
    # 登入成功
    # login_ok = By.XPATH, "//*[contains(@text,'最新')]"
    # login_name = By.XPATH, ("text,账号")
    # login_pwd = By.XPATH, ("text,密码")

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 点击我的
        # 点击登入、注册
        self.click_element("")
        self.click_element("")

    # 输入账号
    def login_name(self, loc, text):
        self.input_element(loc, text)

    # 输入密码
    def login_pwd(self, loc, text):
        self.input_element(loc, text)

    # 点击登入提交
    def click_login(self):
        self.click_element("")



