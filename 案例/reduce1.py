from functools import reduce
#定义一个操作函数
#假如操作函数只是相加
def myAdd(x,y):
    return x+y
#对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst=reduce(myAdd,[1,2,3,4,5,6])#步骤：1+2=3然后3+3=6然后6+4=10然后。。。
print(rst)