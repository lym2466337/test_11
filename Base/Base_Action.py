from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 获取单个元素
    def find_element(self, loc, timeout=10, fre=0.5):
        by = loc[0]
        # 如果 是xpath的方式，通过调用方法拼接xpath路径，而find_elemnt的 loc[1]格式 值需要  "text,设置" 或者一个列表包含多个字符串
        path = loc[1]  # "text,设置"
        if by == By.XPATH:
            path = self.make_xpath_with_feature(path)  # 转换成语句

        return WebDriverWait(self.driver, timeout, fre) \
            .until(lambda x: x.find_element(by, path))

    # 获取多个元素
    def find_elements(self, loc, timeout=5, fre=0.5):
        by = loc[0]
        # 如果 是xpath的方式，通过调用方法拼接xpath路径，而find_elemnt的 loc[1]格式 值需要  "text,设置" 或者一个列表包含多个字符串
        path = loc[1]  # "text,设置"
        if by == By.XPATH:
            path = self.make_xpath_with_feature(path)  # 转换成语句

        return WebDriverWait(self.driver, timeout, fre) \
            .until(lambda x: x.find_elements(by, path))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element(self, loc, text):
        ele = self.find_element(loc)
        ele.clear()
        ele.send_keys(text)

    # 获取toast弹窗
    def find_toast(self, message, is_screen=False, screen_name="screen", timeout=3, fre=0.1):
        message = "//*[contains(@text,'" + message + "')]"

        ele = self.find_element((By.XPATH, message), timeout, fre)
        # 在出现toast窗口时，添加是否进行截图的判断
        if is_screen:
            self.driver.get_screenshot_as_file("./screen/" + screen_name + ".png")

        return ele.text

    # 根据获取toast弹窗 用于断言判断页面是否成功打开
    def is_toast_exit(self, message, is_screen, screen_name, timeout=3, fre=0.1):
        try:
            self.find_toast(message, is_screen, screen_name, timeout, fre)
            return True
        except Exception as e:
            return False

    # xpath路径拼接
    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc
