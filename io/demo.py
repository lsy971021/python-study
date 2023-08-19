class File:
    def readText(self):
        file = open('../doc/content.txt', 'r')
        # 二进制读
        # content = open('../doc/content.txt', 'rb')
        # 读 写
        # content = open('../doc/content.txt', '+')
        print(file.read())
        print('=======')
        file.close()

    def writeText(self, content):
        # 读写
        # open('../doc/content.txt','+')
        # 读 追加写
        file = open('../doc/content.txt','a+')
        # 写
        # open('../doc/content.txt','w')
        # res : 写的长度
        res = file.write(content)
        print(res)
        file.close()

    def readPic(self):
        # rb : 读区 二进制
        file = open("../pic/小男孩.jpg",'rb')
        text = file.read()
        file.close()
        return text

    def copyPic(self,targetPath,content):
        picTargetFile = open(targetPath,'wb')
        picTargetFile.write(content)
        picTargetFile.close()

file = File()

file.readText()
file.writeText('\nGgs')
file.copyPic('../pic/小男孩_copy.jpg',file.readPic())