grades = [90, 100, 82, 70, 59, 61]
gradesLetters = []

for grade in grades:
    if grade >=90:
        gradesLetter = "A"
    elif grade >=80:
        gradesLetter = "B"
    elif grade >=70:
        gradesLetter = "C"
    elif grade >=60:
        gradesLetter = "D"
    else:
        gradesLetter = "F"
    gradesLetters.append(gradesLetter)

print(grades)
print(gradesLetters)
