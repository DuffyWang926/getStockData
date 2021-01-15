import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist

# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyDongCai(code, isCash, stockNum):
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'10',
        'deviceName':'2214c691',
        'appPackage':'com.eastmoney.android.lead',
        'noReset':True,
        'appActivity':'com.eastmoney.android.berlin.activity.MainActivity',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(5)
    if isExist(driver,'com.eastmoney.android.lead:id/riv_card') :
        driver.find_element_by_id('com.eastmoney.android.lead:id/riv_card').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("关闭")').click()
        sleep(1)
   
    driver.find_element_by_android_uiautomator('new UiSelector().text("新股中心")').click()
    sleep(2)
    driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "认购中")]').click()
    sleep(1)
    # if isExist(driver,'com.tigerbrokers.stock:id/btn_cancel') :
    #     driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
    #     sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("IPO")').click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("港股")').click()
    # sleep(1)

    # buyPath='//android.widget.TextView[contains(@text,"(' + code + '.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    # driver.find_element_by_xpath(buyPath).click()
    # sleep(1)
    # if not isCash:
    #     driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()

    # numPath = 'new UiSelector().textContains("%d")'%(stockNum)
    # driver.find_element_by_android_uiautomator(numPath).click()
    # sleep(1)
    driver.quit()