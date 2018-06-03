# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:28:43 2018
快捷键：ctrl+
新建python文件
ctrl +new
保存
执行代码 ctrl 回车
查看版本 python 3.6.2
@author: lenovo
"""
#一次声明一个变量
a=3
#一次申明多个变量
xj="小角"
yanzhi=5.0
print(xj+str(yanzhi))
c='3.9'
d=float(c)

print(xj+'\t'+str(yanzhi))
#字符串中出现{}大括号，表示是否位符
print('今天温度是{}天气是{}今天星期{}'.format(10,'小雨','六'))


#列表list
usemoney=12,20,30,19,20
usemoney[1]
usemoney1=[12,20,30,19,20]
print(usemoney1[0])

##作业一
x=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
for i in x:
    if i=="星期六":
        print("今天是{}".format(i))
        
x=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]

weeks=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
print(weeks[0])
print(weeks[1])
print(weeks[2])
print(weeks[3])
print(weeks[4])
print("今天是："+weeks[5])
print(weeks[6])


msg={"地址":"北京海定区xxx",
 "手机号码":"15202165",
 "寄信人":"chance"
 }
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])


var={"姓名":"张三",
     "身高":"180",
     "性别":"男",
     "年龄":"22",}
print(var["姓名"]+"\n"+var["身高"]+"\n"+var["性别"]+"\n"+var["年龄"])

"""
dict(key:value,...........)
"""


xzq={"name":"薛之谦",
     "songs":["丑八怪","演员","暧昧"],
     "昵称":"小薛",
     "认识过的女朋友":[2,1,3,8,-1]}
songs=xzq["songs"]
print(songs)
print("歌曲总数:"+str(len(songs)))
print(max(xzq["认识过的女朋友"]))

##作业二
wether={"未来五天的温度":[22,28,18,19,23],
        "未来五天的天气情况":["多云","晴","小雨","多云","晴"],
        "日期":["星期一","星期二","星期三","星期四","星期五"]}
wether1=wether["未来五天的温度"]
wether2=wether["未来五天的天气情况"]
wether3=wether["日期"]
print(str(wether1)+"\n"+str(wether2)+"\n"+str(wether3))
print("最高温度："+str(max(wether["未来五天的温度"])))





