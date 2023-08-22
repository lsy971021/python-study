import random


# 梯度下降

# 获取随机 x,y 坐标
def getargs(size, xle=500, yle=2000):
    args = []
    si = int(size)
    for i in range(si):
        x = random.randrange(0, xle)
        y = random.randint(0, yle)
        args.append([x, y])
    return args


# y = wx
# rate: 学习率
# deep: 梯度
# w = w - rate * deep

w = 0.1


def calculate(args):
    add = 0
    print(args)
    for x, y in list(args):
        add += (y - w * x) ** 2
    return add / len(args)


# print(calculate(getargs(100)))


import numpy as np
import matplotlib.pyplot as plt


# 定义函数
def f(x):
    return 3 * x  # 这里以sin函数为例


# 生成x轴数据
x = np.linspace(0, 10, 100)

# 计算对应的y轴数据
y = f(x)

# 绘制函数图
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Plot')
# plt.grid(True)  # 添加网格线
plt.show()

import pyspark
# pyspark.
