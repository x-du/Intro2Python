fibs = [1, 1]
def fib(n):

    for i in range(2,n):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs[n-1]

num = int(input("Give me a number:"))
print("The fibonacci number is", fib(num))
print(fibs)
