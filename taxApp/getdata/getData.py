from selenium.webdriver.common.action_chains import ActionChains
import time
import json
#import models as md
def handle_alert(obj,id):
	obj.click_by_class(id)
	return
def get_data_gs(obj,Dacx_css_selector="a[onclick='goDacx()']",tabelClassName_gs="table[class='table-common']"):

	time.sleep(2)
	obj.click_by_css_selector(Dacx_css_selector)
	time.sleep(3)
	data_arr,dict_gs = obj.get_table_content_gs(tabelClassName_gs)
	obj.driver.close()
	all_hand = obj.driver.window_handles
	obj.driver.switch_to_window(all_hand[0])

	return dict_gs
	#md.saveData(arr2)

def get_data_ds(obj,alert_1=True,Qbgn_css_selector="全部功能",Gzfw_css_selector="icon05",Sfjn_css_selector="a[title='税费缴纳(地税)']",Sscx_css_selecotr="menu_110000_110109",tabelClassName_ds="table[class='table-bordered']",alert_class="layui-layer-btn0"):
	time.sleep(2)
	obj.click_by_link_text(Qbgn_css_selector)#跳其他页面
	all_hand = obj.driver.window_handles
	obj.driver.switch_to_window(all_hand[-1])
	time.sleep(2)
	obj.click_by_class(Gzfw_css_selector)

	time.sleep(2)
	obj.click_by_css_selector(Sfjn_css_selector)#跳其他页面
	time.sleep(2)
	obj.driver.close()
	all_hand = obj.driver.window_handles
	obj.driver.switch_to_window(all_hand[-1])
	if alert_1:
		handle_alert(obj,alert_class)
	obj.click_by_id(Sscx_css_selecotr)
	time.sleep(2)
	obj.driver.switch_to.frame(obj.driver.find_element_by_id("qyIndex"))
	obj.driver.switch_to.frame(obj.driver.find_element_by_id("qymain"))
	dict_ds = obj.get_table_content_ds()
	obj.driver.close()
	all_hand = obj.driver.window_handles
	obj.driver.switch_to_window(all_hand[0])
	return dict_ds



	

	


	