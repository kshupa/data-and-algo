def binary_search(target, lst):

    left = 0
    right = len(lst) - 1
    print(left, right)

    while left <= right:
        midpoint = (left + right) // 2
        if target == lst[midpoint]:
            return midpoint
        elif target < lst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return -1


a = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 7, 7, 7, 7]

print(binary_search(8, a))
