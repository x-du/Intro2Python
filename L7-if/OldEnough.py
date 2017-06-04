driving_age = eval(input("What's the legal driving age in your state?"))
age = eval(input("How old are you? "))

if age >= driving_age:
    print("You are old enough to drive!")
else:
    print("Sorry, you can drive in ", driving_age - age, " years!")
