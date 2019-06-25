# encoding=utf-8
from dointerface.common import comm
# from dointerface.common.parseExcel import ParseExcel
import unittest
import json
import requests
import os
import paramunittest


getRequestInfo_xls= comm.Common().get_xls("data.xlsx","user")
# excelObj=ParseExcel()
# from firstTest import readConfig
# from firstTest.confi.M_log import *
# m_congfig=readConfig.ReadConfig()
@paramunittest.parametrized(*getRequestInfo_xls)
class SignIn(unittest.TestCase):
    # def __init__(self,*args, **kwargs):
    #     unittest.TestCase.__init__(self, *args, **kwargs)
    #     self.case_name='login in'
    #     # self.url=m_congfig.get_http('url')
    #     self.method='post'
    #     self.result=1
    #     self.code='succeed'
    #     self.msg='0'
    #     self.rateText=''
    #     self.return_info={}
    #     self.url='http://mall.api.epet.com/v3/login.html?do=postSubmit'
    #     # print (self.url)
    def setParameters(self,case_name,method,username,password,code,login_status):
        self.case_name = str(case_name)
        # self.url = str(requestUrl)
        self.method = str(method)
        self.username=str(username)
        self.password=str(password)
        self.url="http://mall.api.epet.com/v3/login.html?do=postSubmit"
        self.result=1
        self.code=str(code)
        self.login_status=login_status


    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name+"测试开始前准备")

    def testSignIn(self):
        #set URL
        print("第一步：设置url  "+self.url)
        print(self.url)
        content={'postsubmit':'r9b8s7m4','username':self.username,'password':self.password}
        self.return_json =requests.post(self.url,data=content)
        print("第四步：发送请求\n\t\t请求方法：" + self.method)
        print("第五步：检查结果")
        print(self.return_json.text)
        self.checkResult()

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.return_Info = self.return_json.json()

        # return_data = (json.loads(self.return_json.text))['data']

        #先想一下 通过判断哪些可判断出这个接口返回是正确的
        return_data_alert_target = self.return_Info['alert_target']
        return_code = self.return_Info['code']
        login_status=self.return_Info['login_status']
        print (return_code)
        # return_data_notice = self.return_Info['data']['notice']  #非空
        # return_data_rateText = self.return_Info['data']['rateText']  #非空
        if self.result == 0:
            pass

        if self.result == 1:
           self.assertEqual(self.code, return_code)
           self.assertEqual(self.login_status,login_status)
            # self.assertIn(self.rateText,return_data_rateText)
            # self.assertIsNotNone(return_data_notice)
            # self.assertIsNotNone(return_data_rateText)

if __name__=='__main__':
    print (getRequestInfo_xls)