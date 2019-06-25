# -*- coding:utf-8 -*-
import unittest
from dointerface.Main.HTMLTestRunner import HTMLTestRunner
from dointerface.common.comm import *
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class Test(Common):
    def run(self):
        '''运行测试用例'''
        with open(self.Report, 'wb') as fp:
            discover = unittest.defaultTestLoader.discover \
                    (
                    # os.path.join(os.getcwd(),'cases'),
                    self.fillPath('cases'),
                    pattern='test_*.py'
                )
            HTMLTestRunner(stream=fp, title=u"同步结果", description=u"同步结果").run(discover)


if __name__=='__main__':
    Test().run()