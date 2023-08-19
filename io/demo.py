class File:
    def readText(self, readlength=None):
        file = open('../doc/content.txt', 'r')
        # 二进制读
        # content = open('../doc/content.txt', 'rb')
        # 读 写
        # content = open('../doc/content.txt', '+')
        if readlength == None:
            # 默认读到末尾
            print(file.read())
        else:
            print(file.read(int(readlength)))
        # 会把每一行当作独立一个字符串读到列表中
        # lines = file.readlines()
        # print(lines)
        print('=======')
        # 释放资源
        file.close()

    def readTextForSeek(self, jump=0):
        file = open('../doc/content.txt', 'r')
        print('文件指针当前位置：', file.tell())
        print('开始跳过字符数：', jump)
        # 跳过 jump 个字符进行读取
        file.seek(jump)
        print('文件指针当前位置：', file.tell())
        print('开始读取～')
        print(file.read())
        print('文件指针当前位置：', file.tell())
        file.close()

    def writeText(self, content):
        # 读写
        # open('../doc/content.txt','+')
        # 读 追加写
        file = open('../doc/content.txt', 'a+')
        # 写
        # open('../doc/content.txt','w')
        # res : 写的长度
        res = file.write(content)
        print(res)
        # flush 把缓冲区内容写到磁盘
        # 如果不调用，在close时会自动执行flush 或着 缓冲区中的数据量到到某个值时自动刷到磁盘
        # file.flush()
        print(111)
        # 关闭管道 ，如果关闭后就不能在flush
        file.close()

    def readPic(self):
        # rb : 读区 二进制
        file = open("../pic/小男孩.jpg", 'rb')
        text = file.read()
        file.close()
        return text

    def copyPic(self, targetPath, content):
        picTargetFile = open(targetPath, 'wb')
        picTargetFile.write(content)
        picTargetFile.close()

    def useWith(self):
        # 使用with 可以不用手动关闭资源
        # with 之后 as 之前称为上下文资源
        # with 可以自动管理上下文资源，不论什么原因跳出with 都能确保文件正确的关闭，以此来达到释放资源的目的
        # 如果一个类实现了特殊方法(会自动执行)： __enter__()、 __exit__ 、 称为该类对象遵守了上下文管理协议，该类对象的实例对象称为上下文管理器
        with open("../doc/content.txt", 'r') as file:
            print(file.readline())


file = File()

# file.readText(3)

# file.writeText('\n test~~~~~')

# file.copyPic('../pic/小男孩_copy.jpg',file.readPic())

# file.readTextForSeek(3)

file.useWith()


# 使用with 可以不用手动关闭资源
        # with 之后 as 之前称为上下文资源
        # with 可以自动管理上下文资源，不论什么原因跳出with 都能确保文件正确的关闭，以此来达到释放资源的目的
        # 如果一个类实现了特殊方法(会自动执行)： __enter__()、 __exit__ 、 称为该类对象遵守了上下文管理协议，该类对象的实例对象称为上下文管理器
class ManageContext:
    def __enter__(self):
        print('__enter__被调用了')
        return self
    # 就算执行过程中出现异常  也会执行__exit__
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__被调用了')

    def show(self):
        print('show 被调用了')



def useWith():
    with ManageContext() as context:
        context.show()

useWith()
