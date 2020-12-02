from appium import webdriver
from time import sleep
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '69a5b23d'
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
desired_caps['appActivity'] = '.activities.NavigationActivity'
desired_caps['automationName'] = 'Uiautomator2'
desired_caps['noReset'] = False
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.press_keycode(4)
sleep(2)
driver.press_keycode(4)
sleep(2)
driver.press_keycode(4)
sleep(2)
print(driver.find_element_by_xpath("//*[@text = '再次点击即可退出.']").text)
