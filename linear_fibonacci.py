# linear fibonacci
def fib(n):
    f1 = 0
    f2 = 1
    fn = 1
    if n == 1:
        return 0
    else:
        for i in range(2, n):
            fn = f1 + f2
            f1 = f2
            f2 = fn
    return fn


print(fib(6))

# recursive fibonacci
def rec_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return rec_fib(n - 1) + rec_fib(n - 2)


print(rec_fib(6))
