# lambda 表达式用法
# 1 以lambda开题
# 2 紧跟一定的参数（如果有的话）
# 3 参数后用冒号和表达式主题隔开
# 4 只是一个表达式，所以，没有return
# 计算一个数字的100倍
stm = lambda x:100 * x
#使用上跟函数调用一模一样
print(stm(89))


stm2 = lambda x,y,z:x+y*10+z*100
print(stm2(4,5,6))