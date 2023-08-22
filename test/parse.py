
import json
def read(path):
    file = open(path)
    text = file.read()
    json.load()


# read('../doc/data.html')


file = open("/Users/lsy/Downloads/a.xlsx",'rb')
print(file.read())
