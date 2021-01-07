import os
from time import sleep

import unittest

from appium import webdriver


# Returns abs path relative to this file and not cwd
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )

def buyZunJia(isCash, stockNum):
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'10',
        'deviceName':'2214c691',
        'appPackage':'com.juniorchina.jcstock',
        'noReset':True,
        'appActivity':'.SplashActivity'
    }
    
    # desired_caps['deviceName'] = '2214c691'
    # desired_caps['appPackage'] = 'cn.futu.trader'
    # desired_caps['appPackage'] = 'com.juniorchina.jcstock'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    isCash= True
    stockNum = 4000
    # el = driver.find_element_by_accessibility_id('Graphics')
    # el.click()
    # el = driver.find_element_by_accessibility_id('Arcs')
    # self.assertIsNotNone(el)

    # driver.back()

    # el = driver.find_element_by_accessibility_id("App")
    # self.assertIsNotNone(el)

    # els = driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
    # self.assertGreaterEqual(12, len(els))

    # driver.find_element_by_android_uiautomator('text("API Demos")')
    driver.close_app();            
    sleep(5)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    buyPath='//android.widget.TextView[contains(@text,"(01490.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    driver.find_element_by_xpath(buyPath).click()
    sleep(1)
    if isCash:
        driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()

    numPath = 'new UiSelector().textContains("%d")'%(stockNum)
    driver.find_element_by_android_uiautomator(numPath).click()
    sleep(1)
    # driver.find_element_by_id('com.juniorchina.jcstock:id/tv_ok').click()
    driver.find_element_by_id('com.juniorchina.jcstock:id/tv_cancel').click()
    sleep(5)
    # driver.quit()

