# Time table
# liusy088
#
import random

flag = True

while flag:
    num = input('Choose a number (2-9), or A for all, R for random, Q to quit: ')

    loop = 1
    sign = 0

    if num.isnumeric():
        if int(num) not in range(2, 10):
            continue
    else:

        if num == 'Q':
            flag = False
            continue
        elif num == 'R':
            num = random.randint(2, 9)
        elif num == 'A':
            loop = 10
            num = 2
            sign = 2
        else:
            continue

    while sign < loop:

        print("Times table of", num)
        num = int(num)
        for i in range(1, 10):
            print(num, 'x', i, '=', i * num)
        sign += 1
        num += 1
