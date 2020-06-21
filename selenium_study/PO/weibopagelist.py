from selenium import webdriver
from selenium.webdriver.common.by import By
"""管理搜索结果页面元素"""
class wbplist():
    #pagelist = (By.XPATH,'// *[ @ id = "pl_feedlist_index"] / div[1] / div[1]')
    pagelist = (By.CSS_SELECTOR,'div[action-type="feed_list_item"]')
    title = (By.CSS_SELECTOR, 'p[node-type="feed_list_content"]')
    username = (By.CSS_SELECTOR,'a[class="name"]')
    times = (By.CSS_SELECTOR,'p[class="from"]>a:nth-child(1)')   #nth-child(1)是取a标签里的第1个元素，jquery的用法
    source = (By.CSS_SELECTOR,'p[class="from"]>a:nth-child(2)') #nth-child(2)是取a标签里的第2个元素，jquery的用法
    coll = (By.CSS_SELECTOR,'div[class="card-act"]>ul>li:nth-child(1)')
    send = (By.CSS_SELECTOR,'div[class="card-act"]>ul>li:nth-child(2)')
    comment = (By.CSS_SELECTOR,'div[class="card-act"]>ul>li:nth-child(3)')
    like = (By.CSS_SELECTOR,'div[class="card-act"]>ul>li:nth-child(4)>a>em')


