

from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os

"""测试路径"""
#testcasedir = "./test_case/"

rootpath = '/Users/wangqc/Documents/projects/automation_case/selenium_study/'
testcasedir = os.path.join(rootpath, 'test_case')
print('testcasedir',testcasedir)

def Createsuitel():
    testsuit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcasedir, pattern='testwb_*.py', top_level_dir =None)
    for test_suit in discover:
        for test_case in test_suit:
            testsuit.addTest(test_case)
    return testsuit

print("TESTCASENAME:",Createsuitel())


if __name__ == '__main__':

    SSS = Createsuitel()

    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    filename = rootpath+'report/'+'result'+now_time+'.html'
    print(filename)
    fp = open(filename, 'wb')
    """定义测试报告"""
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告',description='用例执行情况：')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(SSS)

    fp.close

