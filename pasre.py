#!/usr/bin/env python
# -*- coding:utf-8 -*-
key_value_list = []
def output_value(jsons, key):
    """
    通过参数key，在jsons中进行匹配并输出该key对应的value
    :param jsons: 需要解析的json串
    :param key: 需要查找的key
    :return:
    """
    key_value = ""
    key_value_list1 = [1,2,3]
    if isinstance(jsons, dict):
        for json_result in jsons.values():
            if key in jsons.keys():
                key_value = jsons.get(key)
                if len(key_value):
                    print (key_value)
                    key_value_list.append(key_value)
                    print (key_value_list)
            else:
                output_value(json_result, key)
    elif isinstance(jsons, list):
        for json_array in jsons:
            output_value(json_array, key)
    # if len(key_value):
    #     key_value_list.append(key_value)
    return key_value_list

if __name__ =="__main__":
    jsonsstr={"w": "猫香波","wq": "猫香波bobobobo","wor": [{"words":"旺旺"},{"words":"tom"}]}
    out = output_value(jsonsstr, 'words')
    print ("ceshi:",out)
