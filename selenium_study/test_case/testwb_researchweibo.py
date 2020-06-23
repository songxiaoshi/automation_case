# code = 'utf-8'

import unittest

import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

from PO.weibopagelist import wbplist


# from selenium.webdriver.support.wait import WebDriverWait     #显示等待
# from selenium.webdriver.support import expected_conditions as EC #元素的状态是否是可点击的

class researchWeibo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_research(self):
        driver = self.driver
        url = 'https://s.weibo.com/'
        driver.get(url)
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By.CSS_SELECTOR,'div[class="search-input"]>input[type="text"]'))
        # #等待元素出现时马上操作
        driver.find_element(By.CSS_SELECTOR, 'div[class="search-input"]>input[type="text"').send_keys('自动化测试')

        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By.CLASS_NAME,'s-btn-b'))
        driver.find_element(By.CLASS_NAME, 's-btn-b').click()

        # WebDriverWait(self.driver,10).until(EC.visibility_of_element
        # _located(By.XPATH,'// *[ @ id = "pl_feedlist_index"] / div[1] / div[1]'))
        # pagelist = driver.find_element(By.XPATH,'// *[ @ id = "pl_feedlist_index"] / div[1] / div[1]').text
        # p = driver.find_elements(By.CSS_SELECTOR,'div[action-type="feed_list_item"]')

        p = driver.find_elements(*wbplist.pagelist)
        print(p)
        keyword = 'web自动化'
        wb = xlwt.Workbook()
        wt = wb.add_sheet(keyword)
        wt.write(0, 0, '内容')
        wt.write(0, 1, '发送人')
        wt.write(0, 2, '发布时间')
        wt.write(0, 3, '来源')
        wt.write(0, 4, ' 收藏数')
        wt.write(0, 5, '转发数')
        wt.write(0, 6, '评论数')
        wt.write(0, 7, '点赞数')

        counter = 0
        for pl in p:
            counter += 1

            # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(*wbplist.title))
            # title = pl.find_element(By.CSS_SELECTOR, 'p[node-type="feed_list_content"]').text
            # username参数是一个元组，find_element的参数规则是需要2个值，所以需要对传来的元组参数做解包，解包之后就是2个值了

            title = pl.find_element(*wbplist.title).text
            username = pl.find_element(*wbplist.username).text
            times = pl.find_element(*wbplist.times).text
            source = pl.find_element(*wbplist.source).text
            coll = pl.find_element(*wbplist.coll).text
            send = pl.find_element(*wbplist.send).text
            send_num = str(send).split("转发")[1]  # split分割字符串，
            if send_num == '':
                send_num = 0
            comment = pl.find_element(*wbplist.comment).text
            comment_num = str(comment).split("评论")[1]
            if comment_num == '':
                comment_num = 0

            like = pl.find_element(*wbplist.like).text

            print(send_num, comment_num)

            wt.write(counter, 0, title)  # 取标题存到文件
            wt.write(counter, 1, username)  # 取发送人存到文件
            wt.write(counter, 2, times)  # 取发布时间存到文件
            wt.write(counter, 3, source)  # 取来源存到文件
            wt.write(counter, 4, coll)  # 取收藏数存到文件
            wt.write(counter, 5, send_num)  # 取转发数存到文件
            wt.write(counter, 6, comment_num)  # 取评论数存到文件
            wt.write(counter, 7, like)  # 取点赞数存到文件
        wb.save('weibo.xls')

        """
        driver.find_element_by_css_selector('div[class="search-input"]>input[type="text"]').send_keys('web自动化')
        driver.find_element_by_class_name('s-btn-b').click()
        time.sleep(2)
        #eles = driver.find_element_by_css_selector('div[faction-type="feed_list_item"]')
        eles = driver.find_element_by_xpath('// *[ @ id = "pl_feedlist_index"] / div[1] / div[1]').text
        """

        """wb = xlwt.Workbook()
        wt = wb.add_sheet(())
        for ele in eles:
            title = driver.find_element_by_css_selector('p[class="txt"]').text
            username = driver.find_element_by_css_selector('a[class="name"]').text


            print(driver.find_element_by_class_name())"""

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
