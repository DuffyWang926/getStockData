import os
from time import sleep
import unittest
from appium import webdriver
from utils.verify import isExist
from src.getPwdData import getPwd

# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
# following-sibling:: preceding-sibling::
def buyZunJia(param):
    code = param['code']
    isCash = param['isCash']
    stockNum = param['num']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'10',
        'deviceName':'2214c691',
        'appPackage':'com.juniorchina.jcstock',
        'noReset':True,
        'appActivity':'.SplashActivity',
        # 'newCommandTimeout':0,
        'automationName':'uiautomator2'

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
    sleep(2)
    buyPath='//android.widget.TextView[contains(@text,"(' + code + '.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    if isExist(driver,2,buyPath):
        driver.find_element_by_xpath(buyPath).click()
        sleep(1)
        if not isCash:
            driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()
            sleep(1)
        if isCashAll or isFinancingAll:
            maxPath = '//android.widget.TextView[@text="可用资金不足"]/parent::*/parent::*/preceding-sibling::android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView'
            maxExistPath = '//*[@text="可用资金不足"]'
            while not isExist(driver, 2, maxExistPath):
                driver.swipe(200,500,200,100,300)
            maxView = driver.find_element_by_xpath(maxPath)
            maxNum = maxView.text
            maxView.click()
        else:
            numPath = 'new UiSelector().textContains("%d")'%(stockNum)
            if isExist(driver,1,numPath):
                driver.find_element_by_android_uiautomator(numPath).click()
                sleep(1)
        driver.find_element_by_id('com.juniorchina.jcstock:id/tv_ok').click()
        # driver.find_element_by_id('com.juniorchina.jcstock:id/tv_cancel').click()
    pwd = getPwd('zunJia')['tradePwd']
    driver.find_element_by_id('com.juniorchina.jcstock:id/et_password').send_keys(pwd)
    driver.find_element_by_id('com.juniorchina.jcstock:id/layout_commit').click()

    sleep(3)
    driver.quit()