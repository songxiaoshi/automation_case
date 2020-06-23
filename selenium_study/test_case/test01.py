import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import request

#driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#url = 'https://www.baidu.com'
#driver.get(url)
#driver.maximize_window()
#driver.find_element_by_id("kw").send_keys("你好")
#driver.find_element_by_name("wd").send_keys("你好")
#driver.find_element_by_css_selector("#kw").send_keys("1111")   #css定位，copy selector
#driver.find_element_by_css_selector('a[href="https://www.hao123.com"]').click()
#driver.find_element_by_xpath('//*[@id="kw"]').send_keys("hello")    #xpath方法

#driver.find_element_by_class_name('soutu-btn').click()
#driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys("/Users/wangqc/Downloads/软件/测试自动化相关/selenium study/sss.jpg")
#driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
#driver.find_element_by_css_selector('input[type="file"]').send_keys('/Users/wangqc/Downloads/软件/测试自动化相关/selenium study/sss.jpg')
#assert "百度" in driver.title
"""
driver.find_element_by_id('kw').send_keys("hello world")
driver.find_element_by_id('su').click()
time.sleep(4)
result = driver.find_element_by_id('content_left').text
print(result)
assert "hello world" in result
print("good")
"""
class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_baidu_search(self):
        driver=self.driver
        driver.get('http://10.159.41.17:49002/cas/index.html')
        driver.find_element_by_id('kw').send_keys("hello world")
        driver.find_element_by_id('kw').send_keys(Keys.ENTER)
        assert "百度" in driver.title
    def test_bing_rearch(self):
        driver = self.driver
        driver.get("https://www.bing.com")
        driver.find_element_by_id('sb_form_q').send_keys("selenium")
        driver.find_element_by_id('sb_form_q').send_keys(Keys.ENTER)
        assert "Bing" in driver.title
    def tearDown(self):

        self.driver.quit()

if __name__=='__main__':
    unittest.main()

