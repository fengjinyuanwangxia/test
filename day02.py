# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:41:11 2018

@author: lenovo
"""
import urllib.request as r
city_pingyin=input("请输入城市拼音：")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(url.format(city_pingyin)).read().decode('utf-8','ignore')
print(info)


import json
data=json.loads(info)

print("欢迎使用小柚天气app")
print("1.查看当前城市天气，2.查看未来五天的天气")

menno=input("请输入菜单：")

if menno=="1":
    print("查看当前城市天气")
    a=data['main']['temp']
    b=data['weather'][0]["description"]
    c=data['main']['temp_max']
    d=data['main']['pressure']
    print("温度："+str(a))
    print("天气情况:"+b)
    print("最高温度："+str(c))
    print("气压："+str(d))
    
if menno=="2":
    print("未来五天的天气:")
    print("日期："+str(data["list"][0]["dt_txt"]))
    print(str(data["list"][0]['weather'][0]['description'])+";最高温度为:"+str(data["list"][0]["main"]["temp_max"])+";最低温度为:"+str(data["list"][0]["main"]["temp_min"]))
    
    print("日期："+str(data["list"][8]["dt_txt"]))
    print(str(data["list"][8]['weather'][0]['description'])+";最高温度为:"+str(data["list"][8]["main"]["temp_max"])+";最低温度为:"+str(data["list"][8]["main"]["temp_min"]))
    
    print("日期："+str(data["list"][16]["dt_txt"]))
    print(str(data["list"][16]['weather'][0]['description'])+";最高温度为:"+str(data["list"][16]["main"]["temp_max"])+";最低温度为:"+str(data["list"][16]["main"]["temp_min"]))
      
    print("日期："+str(data["list"][24]["dt_txt"]))
    print(str(data["list"][24]['weather'][0]['description'])+";最高温度为:"+str(data["list"][24]["main"]["temp_max"])+";最低温度为:"+str(data["list"][24]["main"]["temp_min"]))
      
    print("日期："+str(data["list"][32]["dt_txt"]))
    print(str(data["list"][32]['weather'][0]['description'])+";最高温度为:"+str(data["list"][32]["main"]["temp_max"])+";最低温度为:"+str(data["list"][32]["main"]["temp_min"]))
   
    
