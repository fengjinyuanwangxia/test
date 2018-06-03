# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request as r
city_pingyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pingyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

print("欢迎使用全球天气app")
print("1.查看当前城市天气，2.查看其他城市的天气，3.保存当前城市")
menno=input("请输入菜单：")

if menno=='1':
    a=data['main']['temp']
    b=data['weather'][0]["description"]
    c=data['main']['temp_max']
    d=data['main']['pressure']
    print("温度："+str(a))
    print("天气情况:"+b)
    print("最高温度："+str(c))
    print("气压："+str(d))
    print("1.查看当前城市天气")

if menno=='2':
    print("2.查看其他城市天气")
if menno=='3':
    print("3.保存当前城市")