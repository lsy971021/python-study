# coding:utf-8

import os

def exec():
    # os.system('../pic/小男孩.jpg')
    # os.startfile('../pic/小男孩.jpg')
    # 当前路径
    print(os.getcwd())
    # 返回路径下文件列表
    print(os.listdir('../'))

def openFile(path):
    os.startfile(path)

def makeDir(dirPath):
    # 创建文件夹
    os.mkdir(dirPath)
    # os.makedirs(dirPath)
    # 删除文件夹
    # os.rmdir(dirPath)
    # os.removedirs(dirPath)
    # 将当前目录设为工作目录
    # os.chdir()

# exec()
# openFile('/Users/lsy/Documents/other/pic/女学生4k动漫壁纸_彼岸图网.jpg')
# makeDir('./test.txt')


# 递归遍历
def walk():
    path = os.getcwd()
    print("pwd:",path)
    # path = '/Volumes/data/code/me/python-study'
    list_file =  os.walk(path)
    print(list_file)
    print('-------')
    for dirpath,dirname,filename in list_file:
        # print(dirpath)
        # print(dirname)
        # print(filename)
        print('==============')
        for dir in dirname:
            # os.path 模块常用操作
            # os.path.join : 将目录与目录或者文件名拼接起来
            # os.path.splitext : 分离文件名和扩展名
            # os.path.basename(name) : 从目录中提取文件名
            print(os.path.join(dirpath,dir))
        print('++++++++++++')
        for file in filename:
            print(os.path.join(dirpath,file))
walk()