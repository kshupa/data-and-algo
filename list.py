lst = ["a", "b", "c", "d"] # stores reference to values
# 4*4 bytes of storage

# access value
print(lst[0])

# search
if 'a' in lst: print(True)
# or
for n in lst:
    if n == 'a':
        print(True)

# insert to the end
lst.append(2)  # O(1)
print(lst)

# insert to beginning
lst.insert(0, "x")  # O(n)
print(lst)

# add 2 lists
lst.extend([3, 4, 5])  #O(k) series of append calls
print(lst)

# delete from end or by index and get it's value
lst.pop()  # O(1)
print(lst)

# delete by value
lst.remove(3)
print(lst)

# remove by index or slice
del lst[1:3]
print(lst)
