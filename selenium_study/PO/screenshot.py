from selenium import webdriver
from PIL import Image,ImageEnhance


def scrshot(self):
        #截取omc系统登录页面的验证码图片
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
