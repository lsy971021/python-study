
age = int(input("Age: "))
student = input("Student (y/n)?")

if age >= 65:
    price = 5
elif age < 5:
    price = 0
elif student == 'y':
    price = 7
else:
    price = 10

print("price: $" + str(price))

