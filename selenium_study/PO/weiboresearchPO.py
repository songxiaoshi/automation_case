from selenium import webdriver
from selenium.webdriver.common.by import By
"""管理搜索页面元素"""
class wbresPO():
    resinput = (By.CSS_SELECTOR,'div[class="search-input"]>input[type="text"]')
    resbutton = (By.CLASS_NAME,'class_name','s-btn-b')
