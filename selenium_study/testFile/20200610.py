code='utf-8'
import unittest
from selenium import webdriver
import time
import requests
from PIL import ImageEnhance,Image
import base64
import pytesseract
import unicodedata
from PO.OCRwenzishibie import OCRshibie
from PO.screenshot import scrshot



class wenzishibieOCR(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_getocrtoken_login(self):
        #获取baidu ocr的accesstoken
        """
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=4D9Fq6ovi4smsk1Y4L5GXnIr&client_secret=MveGFRihFTH0X0cxWqGegBlHRZTqLqOA'
        res = requests.get(host)
        time.sleep(2)
        r = res.json()
        print(r)
        accsee_token = r['access_token']
        print(accsee_token)
        """
        """
        #截取omc系统登录页面的验证码图片
        driver = self.driver
        driver.get('http://10.159.41.17:49002/cas/index.html')
        driver.refresh()
        driver.maximize_window()
        driver.save_screenshot("/Users/wangqc/Downloads/01.png")  # 保存截图
        location = driver.find_element_by_id('captchaImg').location  # 定位验证码控件赋值给变量
        size = driver.find_element_by_id('captchaImg').size  # 取验证码控件大小尺寸
        left = location['x']  # 自动获取验证码坐标
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        ran = Image.open('/Users/wangqc/Downloads/01.png')
        box = (left, top, right, bottom)
        ran.crop(box).save('/Users/wangqc/Downloads/02.png')
        code = Image.open('/Users/wangqc/Downloads/02.png')
        sharp_img = ImageEnhance.Contrast(code).enhance(2.0)
        sharp_img.save('/Users/wangqc/Downloads/03.png')
        time.sleep(2)
        """
        #验证码截图

        driver = webdriver.Chrome()
        driver.get('http://10.159.41.17:49002/cas/index.html')
        driver.refresh()
        driver.maximize_window()
        driver.save_screenshot("/Users/wangqc/Downloads/01.png")  # 保存截图
        location = driver.find_element_by_id('captchaImg').location  # 定位验证码控件赋值给变量
        size = driver.find_element_by_id('captchaImg').size  # 取验证码控件大小尺寸
        left = location['x']  # 自动获取验证码坐标
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        ran = Image.open('/Users/wangqc/Downloads/01.png')
        box = (left, top, right, bottom)
        ran.crop(box).save('/Users/wangqc/Downloads/02.png')
        code = Image.open('/Users/wangqc/Downloads/02.png')
        sharp_img = ImageEnhance.Contrast(code).enhance(2.0)
        sharp_img.save('/Users/wangqc/Downloads/03.png')


        #调用百度鉴权的文字识别接口
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+OCRshibie(self)
        f = open(r'/Users/wangqc/Downloads/03.png','rb')
        img = base64.b64encode(f.read())
        params = {'image':img}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        imageres = requests.post(url,data=params,headers=headers)
        image_json = imageres.json()
        print(image_json)
        words=image_json['words_result'][0]['words']
        print("识别的验证码为：",words)    #打印识别的验证码
        f.close()
        if str.isdigit(words):
            print("识别的字符串为数值")
            if len(words) == 4:
                print("识别的字符串长度为4")

                # 登录

                driver.find_element_by_id('accountName').send_keys('ceshi')
                driver.find_element_by_id('password').send_keys('123456')
                driver.find_element_by_id('captch').send_keys(words)
                driver.find_element_by_id('submit').click()
                time.sleep(2)
                #self.assertIsNotNone(self.driver.find_element_by_css_selector('span[class="name___dJ0yb"]'))
                self.assertIsNotNone(self.driver.find_element_by_class_name('success'))
            else:
                print("识别的字符串长度不正确")
        else:
            print("识别的字符串不全为数值，不正确")

    def tearDown(self):
        pass


if '__name__'=='__main__':
    unittest.main()
