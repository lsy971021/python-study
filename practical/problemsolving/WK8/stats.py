# Statistics
# liusy088


numList = []

userInput = 1

while userInput != 0:
    userIn = input("Number (0 to stop):")
    if userIn.isnumeric():
        userInput = int(userIn)
        if userInput != 0:
            numList.append(userInput)

print(numList)

print('=== Basic statistics ===')

listLen = len(numList)
listSum = sum(numList)

print('Count:', listLen)

if numList:
    print('Minimum:', min(numList))
    print('Maximum:', max(numList))
    print('Total:', listSum)
    print('Average:', round((listSum / listLen), 1))


def average(number_list):
    print('=== Custom functions ===')
    if number_list:
        userList = list(number_list)
        sum = 0
        len = 0
        for i in userList:
            sum += int(i)
            len += 1
        print('My Average: ', round((sum / len), 1))


average(numList)


def maximum(number_list):
    if number_list:
        userList = list(number_list)
        maxNum = userList[0]
        for i in userList:
            if i > maxNum:
                maxNum = i
        print('My Maximum:', maxNum)


maximum(numList)


def offset(number_list, offset_amount):
    print('Offset:', offset_amount)
    if number_list:
        number_list = list(number_list)
        for i in range(0, len(number_list)):
            number_list[i] = number_list[i] + offset_amount
        print('After offset by 5 :', number_list)


offset(numList, 5)
