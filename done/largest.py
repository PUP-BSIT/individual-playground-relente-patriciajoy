#Largest 
def maximum_value(numbers):

  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest

numbers = [] # Get 5 numbers from the user
for i in range(5):
  number = int(input(f"Enter number {i+1}: "))
  numbers.append(number)
max_value = maximum_value(numbers) # Find the maximum value
print("The maximum value is:", max_value)

