def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-2) + f(n-1)


for i in range(100):
    print(f(i))
