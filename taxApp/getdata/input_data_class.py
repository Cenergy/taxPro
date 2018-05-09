import time
class InputDataClass(object):
	def __init__(self,name,driver):
		self.name = name
		self.driver = driver

	def input_by_id(self, text=u'', element_id=''):
		input_el = self.driver.find_element_by_id(element_id) #通过 id 查找网页元素
		input_el.clear()
		input_el.send_keys(text) #输入字符串
		time.sleep(0.5)

	def click_by_id(self, element_id=''):
		search_el = self.driver.find_element_by_id(element_id)
		search_el.click() #鼠标左键单击
		time.sleep(0.5)

	def click_by_class(self, element_class=''):
		search_el = self.driver.find_element_by_class_name(element_class) #通过 class 查找网页元素
		search_el.click() #鼠标左键单击
		time.sleep(0.5)
	def click_by_css_selector(self,element_css_selector=''):
		search_el = self.driver.find_element_by_css_selector(element_css_selector)
		search_el.click()
		time.sleep(0.5)
	def click_by_xpath(self,element_xpath=''):
		search_el = self.driver.find_element_by_xpath(element_xpath)
		search_el.click()
		time.sleep(0.5)
	def click_by_link_text(self,str1=''):
		search_el = self.driver.find_element_by_link_text(str1)
		search_el.click()
		time.sleep(0.5)

	# def getText_by_id(self,id):
	# 	return text
	# def getText_by_class(self,classname):
	# 	return text
	# def getText_by_css_selector(self,css_selector):
	# 	return text

	def get_table_content_gs(self,tabelClassName=""):  
		# 得到selenium打开的浏览器的所有句柄
		all_hand = self.driver.window_handles
		self.driver.switch_to_window(all_hand[-1])

		#处理异常
		arr = []
		dict_1 = {}

		# 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
		table_tr_list = self.driver.find_element_by_css_selector(tabelClassName)
		trs = table_tr_list.find_elements_by_css_selector("tr")
		for tr in trs:
			arr1={}
			ths = tr.find_elements_by_css_selector('th')
			tds = tr.find_elements_by_css_selector('td')
			for i in range(0,len(ths)):
				arr1[ths[i].text] = tds[i].text
				dict_1[ths[i].text] = tds[i].text
			arr.append(arr1)
		return arr,dict_1

	def get_table_content_ds(self,tabelClassName="div[class='message4']>table"):
		# 得到selenium打开的浏览器的所有句柄
		arr = []
		dict_1 = {}
		# 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
		table_tr_list = self.driver.find_element_by_css_selector(tabelClassName)
		trs = table_tr_list.find_elements_by_css_selector("tr")
		for tr in trs:
			arr1={}
			tds = tr.find_elements_by_css_selector('td')
			for i in range(0,len(tds),2):
				pos = tds[i].text.index('：')
				key =(tds[i].text)[0:pos]
				arr1[key] = tds[i+1].text
				dict_1[key]= tds[i+1].text
			arr.append(arr1)
		return dict_1

if __name__ == '__main__':
	pass