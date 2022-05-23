# coding:utf-8
# 首行注释coding用来定义源码的编码格式，python3默认是utf-8
'''
这个是注释
'''
import sys

print('hello world')
point = """三引号可以多行
输出内容
"""
print(point)
name = '刘思远'
print(name)
print('内存地址 =', id(name))
print('类型 =', type(name))
age = 24
print(type(age))
# 不能用加号连接不同数据类型的变量，需要进行类型转换
# print('我叫'+name+'今年'+age+'岁了')
# str() 将其他数据类型转为字符串
print('我叫' + name + '今年' + str(age) + '岁了')
# int() 将其他数据类型转为int,浮点数会截取整数部分，字符串有小数的会报错,布尔类型false为0 true为1
num = '23'
print('age转换前为', type(num), '转换后为', type(int(num)))
strNum = '23.5'
# print('string转换前为',type(strNum),'转换后为',type(int(strNum)),int(strNum))
float = 23.5
print('float转换前为', type(float), '转换后为', type(int(float)), int(float))
boolean = False
print('boolean转换前为', type(boolean), '转换后为', type(int(boolean)), int(boolean))
lists = [11, 22, 33, 44, 55]
print(type(lists))
# 以下均为False，剩下所有对象的布尔值都是true
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

# 支持链式赋值,内存指向一个地址
a = b = c = d = 10  # 将10赋给a b c d
print(a, b, c, d)
b = 11
print(id(a), id(b), id(c), id(d))
# 支持系列解包赋值
e, f, g = 1, 2, 3
print(e, f, g)
e, f, g = f, g, e  # 交换赋值
print(e, f, g)

bool
openIt = False
if openIt:
    # input() 为输入函数，和用户交互 (在控制台输入),默认输入为str
    first = input('请输入第一个数字：')
    second = input('请输入第二个数字：')
    print(first, '+', second + '=', int(first) + int(second))
    # 或者
    first = int(input('请输入第一个数字：'))
    second = int(input('请输入第二个数字：'))
    print(first, '+', second, '=', first + second)

'''
运算符优先级： 幂运算 < 乘除整除取余 < 加减 < 逻辑左移算数右移 < 位与 < 位或 < 比较运算符 < and < or < =
'''
# 运算符有 加 +    减 -    乘 *     除 /     整除 //   取余 &    幂运算 **
print(-9 // 4)  # 一正一负为向下取整
print(9 // 4)  # 同正同负为向上取整
print(-9 % 4)  # 余数 = 被除数-除数*商

# 比较运算符  >   <   >=  <=  !=  ==:对象value的比较   is、is not:id的比较
compare1 = 'aaa'
compare2 = 'aaa'
print(compare1 == compare2)
print(compare1 is compare2, id(compare1), id(compare2))

# 布尔运算符  and   or   not   in   not in
print(False and True)
print(False or True)
print(not True)  # 取反
print('思' in '刘思远')
print('你' not in '刘思远')

# 位运算符  |  &  <<  >>

if openIt:
    # if
    password = int(input("请输入密码:\n"))
    name = '刘思远'
    if password == 111111:
        if name == input('请输入姓名:\n'):
            print('密码输入正确')
        else:
            print('密码输入错误')
    elif password == 222222:
        print('密码输入错误')
    elif 0 >= password >= 999999:
        print('密码输入错误')
    elif int(input('请重试一次')):  # 0 的布尔值为false  大于0为true
        print("hello world")

# 三元表达式
if openIt:

    name = input('请输入姓名\n')
    print('您好好尊贵的刘思远先生' if name == '刘思远' else '您好，先生')

    # pass占位符，当不知道代码写什么时候可用paass替换
    if 'y' == input('你叫刘思远吗?y/n\t'):
        pass
    else:
        print('请滚出去')

# 内置函数 range() 是一个整数序列。有三种创建方式
r1 = range(10)
print(r1)
print(list(r1))  # 对r1展开
r2 = range(1, 10)
print(r2)
print(list(r2))
r3 = range(1, 10, 2)  # 2为间隔
print(r3)
print(list(r3))

print(10 in r3)  # 判断10是否在r3中

num = 1
# 循环  while  && break
while num < 10:
    if num == 8:
        print('结束')
        break
    print(num)
    num += 1

# 循环for in  &  break  & continue   迭代 in 后面的变量
ranges = range(10)
watch = range(3, 5)
for item in ranges:
    if item in watch:
        continue  # 在嵌套循环中 continue 和 break 只用于内层循环，不影响外层
    if item == 8:
        print('结束')
        break
    print(item)
else:  # 当循环语句没有执行执行break就会进入else
    print('全部遍历完成')

# list
lis = ['aa', 'bb', 11, 'dd', 'ff']
lis2 = ['hh', 'ii']
lis.append('gg')
# 将lis2全部添加到lis
lis.extend(lis2)
# 在索引为0的位置增加一个zero,后面的索引依次往后移
lis.insert(0, 'zero')
print(type(lis))
print(lis[0])
# 倒数第三个索引的值
print(lis[-3])
# bb在lis中的索引，当有多个重复元素时只返回第一个 ，若没有此元素则抛异常
print(lis.index('bb'))
# 在索引1到4，不包括4中查找dd的索引位置，若找不到则抛异常
print(lis.index('dd', 1, 5))
# 切片，从lis的1索引开始，4索引结束(不包含4索引),跨度为2进行遍历,默认step跨度为1,切割出来的为新对象，与原id(内存地址)不一样
print(lis[1:4:2])
# start默认为0
print(lis[:4:2])
# stop默认为last
print(lis[1::1])
# start默认、stop默认,step=-1，元素逆序输出
print(lis[::-1])
print(lis[4:0:-1])

lis3 = [11, 22, 33, 44]
lis4 = [666, 777, 888]
# 修改3索引的值
lis3[3] = 66
print(lis3[1:])
# 将1索引后的数据切掉，1索引后面的值替换成33,44,55 或 list4
lis3[1::1] = [33, 44, 55]
lis3[1:] = lis4
print(lis3)
# 在原列表的基础上进行排序，即排序前后内存地址一样
lis3.sort()
# 降序排序
lis3.sort(reverse=True)
# 内置函数sorted进行排序会产生一个新的对象
sorted(lis3)
# 正序排序
sorted(lis3, reverse=False)
# 从列表中移除首个值为11的元素
lis3.remove(11)
print(lis3)
# 删除指定索引的元素，若指定索引不存在则抛异常，若没有参数，则默认删除最后一个元素
lis3.pop(1)
print(lis3)
lis3.pop()
print(lis3)
# 删除列表元素 或 lis3=[]
lis3.clear()
# 删除列表
del lis3

# 列表生成式
# 遍历range依次赋值给i，根据i生成列表 或 根据i的平方生成列表
# i：列表元素的表达式   i：自定义变量   range：可迭代对象
lis5 = [i for i in range(10)]
lis5 = [i * i for i in range(10)]

# 字典  创建有两种方式
dic = {'刘思远': 24, '张三': 10}
print(type(dic))
# 使用内置函数创建, = 左边为key不加引号，右边取决于数据类型
student = dict(name='刘思远', age=24)
print(dic)
print(student)
# 获取字典中的值,若查找的值不存在,[] 方式会报错，get()不会
print(dic['刘思远'])
print(student['name'])
print(student.get('name'))
# get的第二个参数是默认值
print(student.get('gender', '男'))
# 判断是否存在与字典中
print('张三' in dic)
print('张三疯' not in dic)
# 删除
del dic['张三']
# 新增
dic['张三丰'] = 90
print(dic)
# 获取所有键/值/键值对
print(dic.keys())
print(dic.values())
print(dic.items())
# 遍历
for item in dic:
    print(item)

# 将items和price一一对应组合成字典    使用zip函数压缩，以短的元素为基准生成字典
items = ['fruit', 'books', 'others']
prices = [99, 88, 77]
# upper()转换为大写
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)

# 元组  （和字符串一样都为不可变序列 即没有增删改）  相当于Java 的 final
# 元组  和列表相似，只不过元祖为()  列表为[],元祖不能进行增删改
t = ('aa', 'bb', 'cc')
# 若元祖只有一个元素， 逗号不能省
t3 = ('aa',)
# 使用内置函数创建
t1 = tuple(('aa', 'bb', 'cc'))
print(type(t), id(t))
# 获取元组元素
print(t[0])
print(t[1])
print(type(t1), id(t1))

# 集合 （集合是和字典相同的数据结构，无序排列，只有key（相当于java的set），自动去重）
s = {'a', 'b', 'c', 'c', 'c'}
print(s)
# 将range转为set
s1 = set(range(6))
print(type(s1))
# 将列表转为集合
s1 = set([10, 2, 3, 4, 4, 4])
print(s1)
# 集合元素的判断操作
print(2 in s1)
print(2 not in s1)
# add() 一次添加一个元素
s1.add(11)
# update() 一次至少添加一个元素(可添加列表、元组、集合)
s1.update({12, 13})
s1.update([14, 15])
s1.update((17, 16))
print(s1)
# 集合元素的删除操作,若remove一个不存在的元素，会抛异常
s1.remove(11)
print(s1)
# 集合元素的删除操作,若有元素则删除，没有则不抛异常
s1.discard(11)
# 一次只删除一个任意元素
s1.pop()
print(s1)
# 清空集合
s1.clear()
print(s1)

s1 = {11, 22, 33, 55, 44}
s2 = {22, 11, 33, 44, 55}
# 若集合存储内容相同，则为true，与顺序无关
print(s1 == s2)  # true

s3 = {11, 44}
# s3是否为s1的子集
print(s3.issubset(s1))
# s1是否为s3的超集
print(s1.issuperset(s3))
# s1和s3是否 没有 交集
print(s1.isdisjoint(s3))
s3 = {11, 12, 22}
# 输出s1和s3的交集
print(s1.intersection(s3))
print(s1 & s3)
# s1和s3的并集
print(s1.union(s3))
print(s1 | s3)
# s1与s3的差集
print(s1.difference(s3))
print(s1-s3)
#s1和s2的对称差集(与交集相反)
print(s1.symmetric_difference(s3))
print(s1^s3)

#集合生成式(跟列表生成式的不同是 为花括号{})
lis={ i*i for i in range(6)}
print(lis)

#字符串 ， 虽然定义方式不一样，但在内存中的地址是一样的（字符串和元组都为不可变序列）
# 字符串的助留机制 仅保存一份相同且不可变的字符串的方式： 优点 ：当需要要值相同的字符串时可以直接从字符串池中拿，避免频繁的创建和销毁
# 助留机制的几种情况（交互模式：命令交互(在中断执行python3命令打开交互界面)，pyCharm对字符串进行了强制处理，内容相同的会进行助留）：
#       字符串的长度为0或1时、
#       字符合标识符的字符串、
#       字符串只在编译时进行驻留，而非运行时、
#       [-5,256]之间的整数数字
str1 = 'aa'
str2 = "aa"
str3 = '''aa'''
print(str1,id(str1))
print(str2,id(str2))
print(str3,id(str3))
#sys中的intern方法强制2个字符串指向同一个对象
str1=sys.intern(str2)
print(str1 is str2)

s='a'
s1='a'
str4=s+s1
print(id(str4))
# 在需要进行字符串拼接时，建议使用join方法而非+，因为join是先计算出所有字符中的长度，然后再拷贝，只new一次对象，效率比+高
str5=s.join(s1)
print(id(str5))

s='hellow , Python'
# center 居中对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认是空格），若设置宽度小于字符串宽度，则不处理
print(s.center(20,'*'))
# ljust 左对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认是空格），若设置宽度小于字符串宽度，则不处理
print(s.ljust(20,"*"))
# rjust 右对齐，参数如上
print(s.rjust(20,"*"))
# zfill 右对齐，左边用0填充，该方法直接收一个参数，用于指定字符串的宽度，若设置宽度小于字符串宽度，则不处理
print(s.zfill(20))
# split 分割，默认劈分字符是空格字符串，返回的值是一个列表
#       参数sep：指定劈分字符串的劈分符
#       参数maxsplit：指定劈分字符串时最大劈分次数，在经过最大次劈分之后，剩余的子串会作为一部分
# rsplit 从右侧分割，效果同split
print(s.split(sep='o',maxsplit=1))
print(s.rsplit(sep='o',maxsplit=1))