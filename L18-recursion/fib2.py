def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

num = int(input("Give me a number:"))
print("The fibonacci number is", fib(num))
