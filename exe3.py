#Write a program that takes 3 numbers and prints the highest number.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    print("First number is the highest.")
elif num2 > num3:
    print("Second number is the highest.")
else:
    print("Third number is the highest.")