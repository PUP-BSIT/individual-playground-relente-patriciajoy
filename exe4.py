x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
else:
    quadrant = 0
    
print("The point lies in Quadrant", quadrant)