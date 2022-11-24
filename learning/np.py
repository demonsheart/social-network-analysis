import numpy as np

print(np.array([1, 2, 3]))

# 等差序列： np.linspace, np.arange
print(np.linspace(1, 5, 11))  # 起始、终止（包含）、样本个数
print(np.arange(1, 5, 2))  # 起始、终止（不包含）、步长

# 特殊矩阵： zeros, eye, full
print(np.zeros((2, 3)))
print(np.eye(3))  # 3*3的单位矩阵
print(np.eye(3, k=1))  # 偏移主对角线1个单位的伪单位矩阵
print(np.full((2, 3), 10))  # 元组传入大小，10表示填充数值
print(np.full((2, 3), [1, 2, 3]))  # 每行填入相同的列表
target = np.arange(9).reshape(3, 3)
print(target[:-1, [0, 2]])

print(3 * np.ones((2, 2)) + 1)

print(np.array([[2, 3]]))

A = np.arange(1, 10).reshape(3, -1)
print(A)
print((1/A).sum(1).reshape(-1, 1))
print(A*(1/A).sum(1).reshape(-1, 1))


