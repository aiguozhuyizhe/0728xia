# 变量可以赋值
a=100
b=a
print(b)

# 函数名称就是一个变量
def funA():
    print(" In funcA")
funB=funA#把函数funA赋值给funcB
funB()#调用函数funB