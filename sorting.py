def bubbleSort(lst):
    index_len = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(index_len):
            if lst[i] > lst[i + 1]:
                sorted = False
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst


def selection_sort(lst):

    for i in range(len(lst) - 1):
        min_value = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j

        if min_value != i:
            lst[min_value], lst[i] = lst[i], lst[min_value]

    return lst


def insertion_sort(lst):
    index_len = range(1, len(lst))
    for i in index_len:
        value_to_sort = lst[i]

        while lst[i - 1] > value_to_sort and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst


def quick_sort(lst):
    lenght = len(lst)
    if lenght <= 1:
        return

    pivot = lst.pop()
    items_greater = []
    items_middle = []
    items_lower = []

    for item in lst:
        if item > pivot:
            items_greater.append(item)
        elif item == pivit:
            items_middle.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + items_middle + quick_sort(items_greater)


def merge_sort(lst):

    if len(lst) > 1:

        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        merge_sort(lefthalf)
        print("Doing left mergesort")
        merge_sort(righthalf)
        print("Doing right mergesort")

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]

                i += 1

            else:
                lst[k] = righthalf[j]

                j += 1

            k += 1

        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1

    return lst


def check_sorted(A, ascending=True):
    """Check if array is sorted"""

    flag = True
    s = 2 * int(ascending) - 1

    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i]:
            flag = False
            break
    return flag


a = [2, 8, 4, 0, 77, 3, 6619, 74]

print(merge_sort(a))
print(check_sorted(a, ascending=True))
