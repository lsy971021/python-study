# Assignment marking tool
# liusy088
#

report = int(input("Report (0-30): "))
program = int(input("Program (0-70): "))
lateSub = input("Late submission (y/n)? ")

if report < 0 or report > 30 or program < 0 or program > 70:
    print('Marks are not in the valid range.')

else:
    sum = int(report) + int(program)

    print("Report", report, "+", "Program", program, "=", sum)

    if lateSub == 'y':
        sum = int(sum * 0.7 + 0.5)
        print('Late submission (-30%) =', sum)

    marks = 'HD'

    if sum < 40:
        marks = 'F2'
    elif sum < 50:
        marks = 'F1'
    elif sum < 55:
        marks = 'P2'
    elif sum < 65:
        marks = 'P1'
    elif sum < 75:
        marks = 'C'
    elif sum < 85:
        marks = 'D'

    print('Grade:', marks)
