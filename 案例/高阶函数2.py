# 高阶函数举例
# funA是普通函数，返回一个传入数字的100倍

def funA(n):
    return n*100
#再写一个函数，把传入参数乘以300倍，利用高阶函数
def funB(n):
    #最终是想返回300n
    return funA(n) * 3

print(funB(9))

#写一个高阶函数
def funC(n,f):#f 是参数
    #假定函数是把n扩大100倍
    return f(n)*3

print(funC(9,funA))


def funD(n):
    return n*10
#需要吧n放大30倍，此时funB则无法实现
print(funC(9,funD))