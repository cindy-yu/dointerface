# -*- coding:utf-8 -*-
import configparser
import logging
import logging.config
import os
import re,xlrd
import time
import datetime
# from dateutil.relativedelta import relativedelta
from xlrd import open_workbook
from dointerface.runner import MAIN_PATH
class Common(object):
    def fillPath(self,direct):
        # MAIN_PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\common", '')
        # MAIN_PATH=os.path.dirname(os.path.abspath(__file__)).strip("\\common")
        FILE_PATH = (os.path.join(MAIN_PATH, direct),)
        path='/'.join(FILE_PATH)
        print (os.path.abspath(__file__))
        print (MAIN_PATH)
        return path

    @property
    def Report(self):
        '''获取测试报告的生成路径'''
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        return (self.fillPath("Report\\") + now + "Result.html")

    def get_xls(self,xls_name, sheet_name):
        MAIN_PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\common", '')
        cls = []
        testPath=os.path.join(MAIN_PATH,'testData')
        xlsPath = os.path.join(MAIN_PATH, "testData",xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls




if __name__=='__main__':
    a=Common()
    # print a.get_xls("data.xlsx","user")
    print (MAIN_PATH)
    print (a.fillPath('cases'))
    # print type (time.localtime(time.time()))



