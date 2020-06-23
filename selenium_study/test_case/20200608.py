code='utf-8'
from selenium import webdriver
import unittest
import time
from PIL import Image,ImageEnhance   #引用image库，登录时获得验证码会用到

import pytesseract   #识别图片文字
from selenium.webdriver.support.wait import WebDriverWait


class omclogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_login(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.get('http://10.159.41.17:49002/cas/index.html')
        driver.refresh()
        driver.maximize_window()



        """
        #driver.find_element_by_id('accountName').send_keys('ceshi')
        #driver.find_element_by_id('password').send_keys('123456')
        #driver.find_element_by_id('captch').send_keys(vcode)

        """
        driver.save_screenshot("/Users/wangqc/Downloads/01.png")  #保存截图
        location = driver.find_element_by_id('captchaImg').location  #定位验证码控件赋值给变量
        size = driver.find_element_by_id('captchaImg').size      #取验证码控件大小尺寸
        left = location['x']   #自动获取验证码坐标
        top = location['y']
        right = location['x']+size['width']
        bottom = location['y']+size['height']
        ran = Image.open('/Users/wangqc/Downloads/01.png')
        box = (left,top,right,bottom)
        ran.crop(box).save('/Users/wangqc/Downloads/02.png')
        code = Image.open('/Users/wangqc/Downloads/02.png')
        sharp_img = ImageEnhance.Contrast(code).enhance(2.0)
        sharp_img.save('/Users/wangqc/Downloads/03.png')
        time.sleep(2)
        print('输出')
        code1 = pytesseract.image_to_string('/Users/wangqc/Downloads/03.png')  #识别图片文字
        print(code1)  #打印识别的文字，因验证码有干扰所以识别出来的不准确
        print('输出2')
        code2 = pytesseract.image_to_string('/Users/wangqc/Downloads/113.png')  #随意使用本地的图片做识别，图片中有汉字，识别出来的都是英文，应该需要安装tesseract的语言库目前还没有安装，
        print(code2)
        print('输出3')
    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()