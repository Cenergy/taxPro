from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
# import matplotlib.pyplot as plt
import time
# import numpy as np
# import PIL.Image as image
import os,sys,base64,json
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

    def click_validation(self,driver, points):
        p1, p2, p3 = points
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        action = ActionChains(driver)
        elem = driver.find_element_by_id('yzmID2')
        ActionChains(driver).move_to_element(elem).perform()
        time.sleep(1)
        pic = driver.find_element_by_id('yzmpic2')
        chain = action.move_to_element_with_offset(pic, x1, y1).click().move_to_element_with_offset(pic, x2,
                                                                                                    y2).click().move_to_element_with_offset(
            pic, x3, y3).click()
        chain.perform()
        return driver

    def check_passed(self,driver):
        info = driver.find_element_by_id("yzmID2").text
        print(info)
        if info == '验证码正确':
            return True
        else:
            return False

    def input_user_passwd(self,driver, user, passwd):
        action = ActionChains(driver)
        # Input user & passwd
        driver.find_element_by_id('nsrsbh$text').click()
        action.send_keys(user).perform()
        time.sleep(1)
        action = ActionChains(driver)
        driver.find_element_by_id('nsrpwd$text').click()
        action.send_keys(passwd).perform()
        return driver

    def get_data_gs(self,obj, Dacx_css_selector="a[onclick='goDacx()']", tabelClassName_gs="table[class='table-common']"):
        time.sleep(2)
        obj.click_by_css_selector(Dacx_css_selector)
        time.sleep(3)
        try:
            obj.driver.assertTitle("纳税人档案查询")
            print('到达信息处！')
        except Exception as e:
            print("到达信息处失败！")
        data_arr, dict_gs = obj.get_table_content_gs(tabelClassName_gs)
        return dict_gs

    def handle_alert(self,obj, id):
        obj.click_by_class(id)
        return

    def get_data_ds(self,obj, alert_1=True, Qbgn_css_selector="全部功能", Gzfw_css_selector="icon05",
                    Sfjn_css_selector="a[title='税费缴纳(地税)']", Sscx_css_selecotr="menu_110000_110109",
                    tabelClassName_ds="table[class='table-bordered']", alert_class="layui-layer-btn0"):
        time.sleep(2)
        obj.click_by_link_text(Qbgn_css_selector)  # 跳其他页面
        all_hand = obj.driver.window_handles
        obj.driver.switch_to_window(all_hand[-1])

        time.sleep(2)
        obj.click_by_class(Gzfw_css_selector)

        time.sleep(2)
        obj.click_by_css_selector(Sfjn_css_selector)  # 跳其他页面
        time.sleep(2)
        all_hand = obj.driver.window_handles
        obj.driver.switch_to_window(all_hand[-1])
        if alert_1:
            self.handle_alert(obj, alert_class)
        obj.click_by_id(Sscx_css_selecotr)
        time.sleep(2)

        try:
            obj.driver.assertTitle("纳税人档案查询")
            print('到达信息处！')
        except Exception as e:
            print("到达信息处失败！")
        obj.driver.switch_to.frame(obj.driver.find_element_by_id("qyIndex"))
        obj.driver.switch_to.frame(obj.driver.find_element_by_id("qymain"))
        dict_ds = obj.get_table_content_ds()
        obj.driver.switch_to_default_content()
        return dict_ds

if __name__ == '__main__':
    getinf = GetInf("http://dzswj.szgs.gov.cn/BsfwtWeb/apps/views/login/login.html")
    driver = getinf.openbrowser()
    time.sleep(2)
    driver = getinf.input_infos(driver)
    time.sleep(1)
    # yzm64 = getinf.get_yzm64_and_save(driver, 'yzm1.jpg')
    elem = driver.find_element_by_class_name('loginBtn').click()
    # bb = "(123,11),(32,45),(56,98)"
    # cc = [(int(x), int(y)) for x, y in [x.replace(')', '').replace('(', '').split(',') for x in bb.split('),(')]]
    # driver1=getinf.click_validation(driver,cc)
    # time.sleep(2)
    # getinf.check_passed(driver1)
