def inch2cm(inches):
    return inches*2.54

def lb2kg(pounds):
    return pounds/2.2

height_in = int(input("Enter your height in inches: "))
weight_lb = int(input("Enter your weight in pounds: "))

height_cm = inch2cm(height_in)
weight_kg = lb2kg(weight_lb)

pingpong_tall = round(height_cm / 4)
pingpong_heavy = round(weight_kg*1000 / 2.7)

feet = height_in // 12
inch = height_in % 12

print("You are ", feet, "feet and", inch, "inches tall, and", weight_lb, "pounds.")
print("You measure", pingpong_tall, "Ping-Pong balls tall. ")
print("You weigh the same as ", pingpong_heavy, "Ping-Pong balls!")
