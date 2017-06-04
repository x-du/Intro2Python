grade = eval(input("Enter your number grade: (0 - 100): "))
if grade >=90:
    gradeLetter = "A"
elif grade >=80:
    gradeLetter = "B"
elif grade >=70:
    gradeLetter = "C"
elif grade >=60:
    gradeLetter = "D"
else:
    gradeLetter = "F"
print("You got", gradeLetter)
