from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
# import matplotlib.pyplot as plt
import time
# import numpy as np
# import PIL.Image as image
import os,sys,requests,base64,json
class GetInf:
    def __init__(self,url):
        self.url=url
    def getinf(self):
        url=self.url
        return url
    def openbrowser(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver

    def input_infos(self,driver):
        action = ActionChains(driver)
        elem = driver.find_element_by_id('shlogin')
        ActionChains(driver).move_to_element(elem).click().perform()
        return driver

    def get_yzm64_and_save(self,driver, to_file):
        info = driver.find_element_by_id("yzmID2").text
        elem = driver.find_element_by_class_name('row')
        ActionChains(driver).move_to_element(elem).perform()
        pic = driver.find_element_by_id('clickTipCaptcha2')
        img64 = pic.get_attribute('src')[22:]
        with open(to_file, 'wb') as f:
            f.write(base64.b64decode(img64))
        return img64,info



if __name__ == '__main__':
    getinf = GetInf("http://dzswj.szgs.gov.cn/BsfwtWeb/apps/views/login/login.html")
    driver = getinf.openbrowser()
    time.sleep(2)
    driver = getinf.input_infos(driver)
    time.sleep(1)
    yzm64 = getinf.get_yzm64_and_save(driver, './img/yzm1.jpg')
