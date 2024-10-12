#Write a program that takes a 2 digit number and returns the sum of the 2 digits. Ex. 24 -> 6

num = int(input("Enter a 2-digit number: "))

digit1 = num // 10
digit2 = num % 10

sum_of_digits = digit1 + digit2

print(f"The sum of the digits is: {sum_of_digits}")