import os
from time import sleep
import unittest
from appium import webdriver

# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyZunJia(code, isCash, stockNum):
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'10',
        'deviceName':'2214c691',
        'appPackage':'com.juniorchina.jcstock',
        'noReset':True,
        'appActivity':'.SplashActivity'
    }
    
    # desired_caps['appPackage'] = 'cn.futu.trader'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(5)
    driver.launch_app(); 
    sleep(5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    sleep(1)
    buyPath='//android.widget.TextView[contains(@text,"(' + code + '.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    driver.find_element_by_xpath(buyPath).click()
    sleep(1)
    if not isCash:
        driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()

    numPath = 'new UiSelector().textContains("%d")'%(stockNum)
    driver.find_element_by_android_uiautomator(numPath).click()
    # driver.find_element_by_id('com.juniorchina.jcstock:id/tv_new_stock_amount').click()
    sleep(1)
    # driver.find_element_by_id('com.juniorchina.jcstock:id/tv_ok').click()
    # driver.find_element_by_id('com.juniorchina.jcstock:id/tv_cancel').click()
    sleep(3)
    driver.quit()