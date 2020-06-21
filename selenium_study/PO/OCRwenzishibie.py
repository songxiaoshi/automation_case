from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

def OCRshibie(self):
    #获取baidu ocr的accesstoken
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=4D9Fq6ovi4smsk1Y4L5GXnIr&client_secret=MveGFRihFTH0X0cxWqGegBlHRZTqLqOA'
    res = requests.get(host)
    time.sleep(2)
    r = res.json()
    print(r)
    accsee_token = r['access_token']
    #print(By.accsee_token)
    return  accsee_token


