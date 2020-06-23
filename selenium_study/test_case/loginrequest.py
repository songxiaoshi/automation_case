coding='utf-8'

import unittest
import requests
from selenium import webdriver
import time
import os


class loginRequest(unittest.TestCase):
    def setUp(self) :
        pass
    def test_login(self):
        url = "http://10.159.41.17:49001/api/cas/login"
        data = {'username':'ceshi','password':'123456','verifyCode':'4315'}
        #data ="df9a9b3f08824d5fafab0ad0994a74e1"
        result = requests.get(url,data=data)
        print(1)
        print(result)
        print(2)
        print(result.text)
        print(3)
        print(result.content)


    def tearDown(self):
        pass

if  '__name__'=='__main__':
    unittest.main()