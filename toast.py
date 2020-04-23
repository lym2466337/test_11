from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desire_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '7.1.2',  # 手机安卓版本
        'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
        'appPackage': 'com.obestseed.ku',  # 启动APP Package名称
        'appActivity': 'net.ku.ku.activity.login.LoginActivity',  # 启动Activity名称
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App，特别注意 对于启动缓慢的APP，需要先打开过APP后，再使用软件打开APP才能正常打开
        'newCommandTimeout': 6000,  # 设置等待APP无响应时间,必须设置
        #toast必须使用 Uiautomator2 才可以获取
        'automationName': 'UiAutomator2'
    }
driver= webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)


def find_toast(message):
    ele=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element(By.XPATH,"//*[contains(@text,'"+message+"')]"))
    print(ele.text)

def test111():
    WebDriverWait(driver,5,0.5).until(lambda x:x.find_element(By.XPATH,"//*[contains(@text,'账号')]")).click()

    ele.send_keys("xxx")

if __name__ == '__main__':
    test111()
    driver.quit()