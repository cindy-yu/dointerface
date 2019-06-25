# -*- coding:utf-8 -*-
import re
def my_Match():
    words = '盛装的仅仅是半杯水，遇见的那个人依然似乎无法填补内心的一点一点地蒸发掉，蒸发掉部期待馋嘴猫配方'
    regex_str = ".*?([\u4E00-\u9FA5]+馋嘴猫配方)"
    match_obj = re.match(regex_str, words)
    if match_obj:
        print(match_obj.group(1))
    else:
        print("cannot match")

def getIndexOfValue(str1,str2):
    target=str2.split(',')
    for i in range(len(target)):
        print(target[i])
    if str1==None or str2==None:
        return 0
    elif str1==str2:
        print("the same")
        return 1
    else:
        for i in range(3):
            if str1==target[i]:
                return i
            else:
                print ("not found")
        return 2

if __name__=='__main__':
    getIndexOfValue('hu,jian,ji','hu,jian,ji')