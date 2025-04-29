items = ['apple', 'jam', 'bread']
# print(items)

add = input('What would you like to add? ')

items.append(add)


print("=== Shopping List ===")

for item in items:
    print(item)