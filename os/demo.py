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
openFile('/Users/lsy/Documents/other/pic/女学生4k动漫壁纸_彼岸图网.jpg')
# makeDir('./test.txt')