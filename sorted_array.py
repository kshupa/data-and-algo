# mergeSortedArrays([0,3,4,31] [4,6,30])

list1 = [0, 3, 4, 31]
list2 = [4, 6, 30]

# merged_list = list1 + list2
# print(sorted(merged_list))


# def mergeSortedArrays(array1, array2):
#     for i in range(len(array2)):
#         item = array2.pop()
#         array1.append(item)
#     return array1


# print(sorted(mergeSortedArrays(list1, list2)))

# 3 method
def mergeSortedArrays2(arr1, arr2):
    # check input
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    merged_array = []
    index1 = index2 = 0

    while index1 < len(arr1):
        if arr1[index1] < arr2[index2]:
            merged_array.append(arr1[index1])
            index1 += 1
        else:
            merged_array.append(arr2[index2])
            index2 += 1
    return merged_array


print(mergeSortedArrays2(list1, list2))
