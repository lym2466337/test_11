from selenium.webdriver.common.by import By

from Base.Base_Action import BaseAction


class Login(BaseAction):
    # 登入成功
    login_ok = By.XPATH, ("text,添加")
    login_name1 = By.CLASS_NAME, "android.widget.LinearLayout"
    login_pwd1 = By.XPATH, ("text,密码")

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # # 点击登入
        # self.click_element((By.XPATH,"text,本机号一键登录"))

    # 输入账号
    def login_name(self, text):
        self.input_element(self.login_name1, text)

    # 输入密码
    def login_pwd(self, login_pwd1, text):
        self.input_element(self.login_pwd1, text)

    # 点击登入提交
    def click_login(self):
        self.click_element(self.login_ok)



