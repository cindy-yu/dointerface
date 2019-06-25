# -*- coding:utf-8 -*-
import sys
import os
global MAIN_PATH
MAIN_PATH=os.path.abspath(os.path.dirname(__file__))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# import timer
from dointerface.Main.main import *
def start_case():
    Test().run()
if __name__=='__main__':
    start_case()
    # path=os.path.join(os.getcwd(),'dointerface')
    # path=os.getcwd()
    # print path
