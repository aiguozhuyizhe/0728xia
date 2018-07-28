# map 举例
#  有一个列表，想对列表里的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]

print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)


# 利用map是实现

def mulTen(n):
    return n * 10


# map类型是一个可迭代的结构，所以可以使用for遍历
l3 = map(mulTen, l1)
for i in l3:
    print(i)

# 以下列表生成式得到的结果为空，why？
l4 = [i for i in l3]
print(l4)