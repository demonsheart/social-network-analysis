# 列表推导与条件
# L = []

# def my_func(x):
#     return 2*x

# for i in range(5):
#     L.append(my_func(i))

# print(L)

# print([my_func(i) for i in range(5)])

# print([m+'_'+n for m in ['a', 'b'] for n in ['c', 'd']])

# print('cat' if 2<1 else 'dog')

# print([i if i<=5 else 5 for i in range(10)])


# 匿名函数与map方法
my_func = lambda x, y: 2 * x + y

print(my_func(2, 3))

print([(lambda x: 2 * x)(i) for i in range(5)])

print(list(map(lambda x: 2 * x, range(5))))

print(list(map(lambda x, y: str(x) + '_' + y, range(5), list('abcde'))))

# zip函数 emumerate方法

# zip函数能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个 zip 对象，通过 tuple, list 可以得到相应的打包结果：
L1, L2, L3 = list('abc'), list('def'), list('hij')
print(list(zip(L1, L2, L3)))
print(tuple(zip(L1, L2, L3)))

for i, j, k in zip(L1, L2, L3):
    print(i, j, k)

# enumerate 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号
L = list('abcd')
for index, value in enumerate(L):
    print(index, value)

# 当需要对两个列表建立字典映射时，可以利用 zip 对象：
print(dict(zip(L1, L2)))

# 既然有了压缩函数，那么 Python 也提供了 * 操作符和 zip 联合使用来进行解压操作：
zipped = list(zip(L1, L2, L3))
print(zipped)  # [('a', 'd', 'h'), ('b', 'e', 'i'), ('c', 'f', 'j')]
print(list(zip(*zipped)))  # [('a', 'b', 'c'), ('d', 'e', 'f'), ('h', 'i', 'j')]
