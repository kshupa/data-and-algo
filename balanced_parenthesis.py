def is_match(par1, par2):

    if par1 + par2 in ['{}', '[]', '()']:
        return True
    else:
        return False


def balanced_paren(s):
    
    index = 0
    is_balanced = True
    opening = '[{('
    stack = []

    while index < len(s) and is_balanced:

        if s[index] in opening:
            stack.append(s[index])

        else:
            if stack == []:
                is_balanced = False

            else:
                last = stack.pop()

                if not is_match(s[index], last):
                    is_balanced = False

        index += 1

    if stack == [] and is_balanced:
        return True

    else:
        return False


print(balanced_paren('[]{}()()'))