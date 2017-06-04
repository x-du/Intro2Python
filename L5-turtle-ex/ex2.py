'''
Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    Write a loop that prints each of the numbers on a new line.
    Write a loop that prints each number and its square on a new line.
    Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.
    Print the product of all the numbers in the list. (product means all multiplied together)
'''
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

def print1():
    for i in xs:
        print(i)

def print2():
    for i in xs:
        print(i**2)

def print3():
    total = 0
    for i in xs:
        total = total + i
    print(total)

def print4():
    product = 1
    for i in xs:
        product = product * i
    print(product)

print("Solution 1")
print1()
print("Solution 2")
print2()
print("Solution 3")
print3()
print("Solution 4")
print4()
