# img = open("/Users/lsy/Downloads/WechatIMG252.jpeg", 'r')

# print(img)

f = lambda x, y: print(x + y)

f(1, 2)
class AAA(object):
    def __init__(self,a,aa):
        self.a=a
        self.aa=aa
    def aaa(self):
        print('AAA中的a()')

class BBB(object):
    def __init__(self,b,bb,j):
        self.b=b
        self.bb=bb
        self.j=j
    def aaa(self):
        print('BBB中的a()')

    def bbb(self):
        print('BBB中的b()')



a=10
b=10
print(a is b)
