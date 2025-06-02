# Practical 12 - Common algorithms
# liusy088
#

# Step 1
def bubble_sort(numbers):
    """Sort the list numbers in ascending order using Bubble sort algorithm."""
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Sorted:", numbers)

# Step 2
def binary_search(numbers, target):
    """Return the index of the target in list numbers. Return -1 if not found."""
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Step 3
def depth_first(tree, node):
    """Traverse the tree from node in depth-first order."""
    print(tree[node]["data"])
    for child in tree[node]["children"]:
        depth_first(tree, child)

def breadth_first(tree, root_node):
    """Traverse the tree from root_node in breadth-first order."""
    from collections import deque
    queue = deque([root_node])
    while queue:
        current = queue.popleft()
        print(tree[current]["data"])
        for child in tree[current]["children"]:
            queue.append(child)

def main():
    numbers = [53, 22, 79, 17, 83, 11, 40, 36]

    # Step 1
    print("=== Bubble Sort ===")
    print(numbers)
    bubble_sort(numbers)
    print()

    # Step 2
    print("=== Binary Search ===")
    print("Index of 40:", binary_search(numbers, 40))
    print()
    print("Index of 12:", binary_search(numbers, 12))
    print()

    # Step 3
    # A tree with node 1 as the root node.
    tree = {
        1: {'data': 'Apple', 'children':[2,3,4] },
        2: {'data': 'Banana', 'children':[5,6] },
        3: {'data': 'Cherry', 'children':[7] },
        4: {'data': 'Grape', 'children':[] },
        5: {'data': 'Melon', 'children':[] },
        6: {'data': 'Orange', 'children':[] },
        7: {'data': 'Pear', 'children':[] },
    }

    print("=== Depth First Traverse ===")
    depth_first(tree, 1)
    print()

    print("=== Breadth First Traverse ===")
    breadth_first(tree, 1)


main()
