from appium import webdriver


def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '69a5b23d'
    desired_caps['appPackage'] = 'com.csc.aolaigo'
    desired_caps['appActivity'] = '.ui.MainActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)