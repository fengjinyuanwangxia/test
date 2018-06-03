# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:41:11 2018

@author: lenovo
"""
import urllib.request as r

print("欢迎使用小柚天气app")

a=input("是否第一次登陆：")
if a=="no":
    print("登录成功")
else:
    print("欢迎第一次使用，请登记你的名字")
    print("注册")


city_pingyin=input("请输入城市拼音：")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(url.format(city_pingyin)).read().decode('utf-8','ignore')
print(info)


import json
data=json.loads(info)


print("1.查看未来五天的天气,2.查看其他城市天气,3.保存")

menno=input("请输入菜单：")

    
if menno=="1":
    print("未来五天的天气:")
    for i in range(0,36):
        print("日期："+str(data["list"][i]["dt_txt"]))
        print(str(data["list"][i]['weather'][0]['description'])+";最高温度为:"+str(data["list"][i]["main"]["temp_max"])+";最低温度为:"+str(data["list"][i]["main"]["temp_min"]))

if menno=="2":
    print("查看其他城市天气")

if menno=="3":
    print("保存")
