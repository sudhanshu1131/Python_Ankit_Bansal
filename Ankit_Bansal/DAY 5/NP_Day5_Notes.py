# #functions
# # def greet():
# #     print("Good Morning")
#
# num=4
# def getsum(a,b):
#     num=a+b
#     return num
#
# d=getsum(1,5)
# print(d)
# print(num)
#
#
# def getsum(a,b):
#     num=a+b
#     return num
# def getsum3(*args):
#     print(args,type(args))
#     num=0
#     for a in args:
#         num=num+a
#     return num
#
# d=getsum3(1,2,3)
#
# def getsum(a,b):
#     print(a,type(a))
#
# d= getsum(b=1.0,a=2)
#
#
# def getsum3(**kwargs):
#     print(kwargs,type(kwargs))
#     print('name', kwargs['name'])
#
#
# d=getsum3(id=24,name='Rahul',age=35)
#from mypackage import calc as c
#import mypackage.calc as c
from mypackage.calc import mgetsum
import mypackage.calc2 as c2
#print(m(1,2))
print(c2.mgetsub(1,2))
a='abc'

a=[1,2,3]
b=[1,2,3,4]
#c = sum(a)/len(a)

def getmean(a):
    return sum(a)/len(a)

print(getmean(a))
print(getmean(b))

import os
os.listdir()
import datetime as dt

dt.datetime.today().strftime('%Y-%m-%d')

import pandas as pd

def getsum3(*args,**kwargs):
    print(args, type(args))
    print(kwargs,type(kwargs))


d=getsum3(1,2,3,a=2,b=2,c=3)

c=10
def var(a,c):
    global c
    c=c+a
    print(c)
var(2,3)
print(c)


