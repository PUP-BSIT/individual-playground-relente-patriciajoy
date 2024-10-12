#Write a program that takes a a coordinate and tell which quadrant the coordinate falls.

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
else:
    quadrant = 0
    
print(f"The coordinate falls in Quadrant {quadrant}")