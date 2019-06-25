# encoding=utf-8
from dointerface.common import comm
# from dointerface.common.parseExcel import ParseExcel
import unittest
import json
import requests
import os
import paramunittest
getRequestInfo_xls= comm.Common().get_xls("data.xlsx","order")

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
    def setParameters(self,case_name,method,url,value,checked,code,list):
        self.case_name = str(case_name)
        # self.url = str(requestUrl)
        self.method = str(method)
        self.url = str(url)
        self.value=str(value)
        self.checked = str(checked)
        self.code = code
        self.cookie = ''
        self.list = str(list)
        self.key_value_list = []


    def description(self):
        """
        test report description
        :return:
        """
        print ("description")

    def setUp(self):
        """
        :return:
        """
        url_login = "http://mallapi.dev.epet.com/v3/login.html?do=postSubmit"
        content_login = {'postsubmit': 'r9b8s7m4', 'username': '胡建骥 ', 'password': '123456'}
        login = requests.post(url_login, data=content_login)
        print(login.json())
        self.cocookies = login.cookies
        print("测试开始前准备")

    def testOrder(self):
        #set URL
        print("第一步：设置url  " + self.url)
        print(self.url)
        content = {'value': self.value, 'checked': self.checked}
        self.return_json = requests.post(self.url, data=content,cookies=self.cocookies)
        print("第二步骤：发送请求\n\t\t请求方法：" + self.method)
        print("第三步骤：检查结果")
        print(self.return_json.text)
        self.checkResult()

        # check result
        # self.tearDown()
        print ("testSignIn")

    def output_value(self,jsons, key):
        """
        通过参数key，在jsons中进行匹配并输出该key对应的value
        :param jsons: 需要解析的json串
        :param key: 需要查找的key
        :return:
        """
        key_value = ""
        if isinstance(jsons, dict):
            for json_result in jsons.values():
                if key in jsons.keys():
                    key_value = jsons.get(key)
                    if len(key_value):
                        print(key_value)
                        self.key_value_list.append(key_value)

                else:
                   self.output_value(self,json_result, key)
        elif isinstance(jsons, list):
            for json_array in jsons:
                self.output_value(json_array, key)
        # if len(key_value):
        #     key_value_list.append(key_value)
        return self.key_value_list



    def checkResult(self):
        """
        check test result
        :return:
        """
        self.return_Info = self.return_json.json()

        # return_data = (json.loads(self.return_json.text))['data']

        #先想一下 通过判断哪些可判断出这个接口返回是正确的
        # return_data_alert_target = self.return_Info['alert_target']
        jsons=json.loads(self.return_code)
        m_list=self.output_value( jsons,'crm_v3')
        return_code = self.return_Info['code']
        print (return_code)
        # return_data_notice = self.return_Info['data']['notice']  #非空
        # return_data_rateText = self.return_Info['data']['rateText']  #非空
        self.assertEqual(self.code, return_code)
        self.assertEqual(self.list,m_list)
        print("checkResult")



if __name__=='__main__':
    print ("123")
