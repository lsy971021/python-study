

class read:
    def __init__(self):
        self.content = open("../doc/content.txt", "r")
        self.html = open("../doc/content.txt", "r")

    def print(self):
        print(self.html.read())
        print(self.content.read())

print(read().print())



