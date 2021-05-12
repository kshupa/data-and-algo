lst = ["a", "b", "c", "d"]

# 4*4 bytes of storage
# add

lst.append("e")  # O(1)
print(lst)

# pop

lst.pop()  # O(1)
print(lst)

# add to beginning

lst.insert(0, "x")  # O(n)
print(lst)
