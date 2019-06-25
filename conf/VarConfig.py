# encoding='utf-8'
import os
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pageElementLocatorPath=parentDirPath+u"\\conf\\PageElementLocator.ini"
dataFile = parentDirPath+u"\\testData\\data.xlsx"
case_name = 1
method = 2
username = 3
password = 4
code = 5
login_status=6

if __name__=='__main__':
    print (dataFile)
    print (pageElementLocatorPath)