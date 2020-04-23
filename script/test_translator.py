import sys, pytest, allure

sys.path.append("E:\python\Po_test1")

from Base.init_driver import init_driver
from Page.page import Page
from Base.Base_yml import get_yml_with_filename_key


class Test_Trans():
    def setup_class(self):
        self.driver = init_driver()
        self.trans_obj = Page(self.driver).get_trans()

    @allure.step(title="这是登录测试")
    @pytest.mark.parametrize("dir", get_yml_with_filename_key("trans_data", "TestData"))
    def test_001(self, dir):
        name = dir["name"]
        phone = dir["phone"]

        allure.attach("输入姓名", name)
        self.trans_obj.input_name(name)

        allure.attach("输入电话", phone)
        self.trans_obj.input_phone(phone)

        allure.attach("提交")
        self.trans_obj.click_submit()



    # def test_002(self):
    #     print(111)
    def teardown_class(self):
        self.driver.quit()
