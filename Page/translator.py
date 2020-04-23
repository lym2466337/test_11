from time import sleep

from selenium.webdriver.common.by import By

from Base.Base_Action import BaseAction


class Trans(BaseAction):
    # 登入成功
    trans_add = By.ID,"com.android.contacts:id/floating_action_button"
    trans_name = By.XPATH, ("text,姓名")
    trans_phone = By.XPATH, ("text,电话")
    trans_submit= By.ID,"com.android.contacts:id/menu_save"


    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 输入姓名
    def input_name(self, text):
        #点击添加
        self.click_element(self.trans_add)
        self.input_element(self.trans_name, text)

    #输入电话
    def input_phone(self, text):
        self.input_element(self.trans_phone, text)

    # 点击提交
    def click_submit(self):
        self.click_element(self.trans_submit)
        sleep(2)
        self.driver.press_keycode(4)



