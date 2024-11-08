#Sum
def sum_value(numbers):
    
  sum = 0
  for number in numbers:
    sum += number
  return sum
numbers = []  # Get 5 numbers from the user
for i in range(5):
  number = int(input(f"Enter number {i+1}: "))
  numbers.append(number)
sum_value = sum_value(numbers)  # Find the sum value
print("The sum of the values is:", sum_value)