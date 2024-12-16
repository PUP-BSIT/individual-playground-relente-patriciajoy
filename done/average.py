#Average
def avg_value(numbers):

  sum_of_numbers = sum(numbers)
  average = sum_of_numbers / len(numbers) #sum of the numbers divided by the length
  return average

numbers = [] # Get 5 numbers from the user
for i in range(5):
  number = int(input(f"Enter number {i+1}: "))
  numbers.append(number)

average_value = avg_value(numbers)
print("The average of the values is:", average_value)
