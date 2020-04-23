import sys, pytest,allure

sys.path.append("E:\python\Po_test1")

from Base.init_driver import init_driver
from Page.page import Page
from Base.Base_yml import get_yml_with_filename_key


class Test_Login():
    def setup_class(self):
        self.driver = init_driver()
        self.login_obj = Page(self.driver).get_login()

    # 输入手机号码
    # 输入密码
    # 判断页面登入是否成功：使用断言方法
    # 每次传入参数直接为一个 列表，可以直接对应3个参数
    # 这种方式 用的比较少，在数据量比较少可以用，但是yml书写比较模糊
    # @pytest.mark.parametrize(("name","pwd","toast"),get_data("TestData"))
    # def test_login(self,name,pwd,toast):
    #     self.login_obj.login_name(name)
    #     self.login_obj.login_pwd(pwd)
    #     self.login_obj.click_login()
    #
    #     assert self.login_obj.is_toast_exit(toast)
    #
    #     print('xxxx')

    # 每次传入的参数是一个字典，使用时需要根据字典的键获取对应值
    # 这种方法用的比较多，因为yml的书写格式 很清晰
    @allure.step(title="这是登录测试")
    @pytest.mark.parametrize("dir", get_yml_with_filename_key("login_data", "TestData2"))
    def test_login2(self, dir):
        name = dir["name"]
        password = dir["password"]
        toast = dir["toast"]

        #当有需要新增参数数据时，可以自己再加入yml，读取格式无需修改，很方便
        screen = dir["screen"]

        allure.attach("输入用户名", name)
        self.login_obj.login_name(name)

        allure.attach("输入密码", password)
        self.login_obj.login_pwd(password)

        allure.attach("点击登入")
        self.login_obj.click_login()

        allure.attach("登入结果判断", toast)
        #断言判断，并且进行截图
        # toast_exist= self.login_obj.is_toast_exit(toast,True,screen)
        # #将截图上传到报告中
        # allure.attach("图片",open("./screen/"+screen+".png","rb").read(),allure.attachment_type.PNG)
        # assert toast_exist
    
    def test_001(self):
        print(111)
    def teardown_class(self):
        self.driver.quit()
