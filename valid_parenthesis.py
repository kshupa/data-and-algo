s = "{[]}"

i = 0
open_stk = []
closed_stk = []

while i < len(s):
    if s[i] == "(" or "[" or "{":
        open_stk.append(s[i])
    if s[i] == ")" or "]" or "}":
        closed_stk.pop(s[i])

    i = i + 1

print(open_stk)
print(closed_stk)