numbers = [1,2,3,4,5,6,7,8,9,0]

# Double only evens
# Takes in a list of numbers and doubles and returns only evens

def double_only_evens(nums):
  output = []
  for num in nums:
    if num % 2 == 0:
      output.append(num*2)
  
  return output

doubled_evens = double_only_evens(numbers)
print(doubled_evens)

# Combining Map and filter

doubled_evens_map_filter = list(map(lambda num: num * 2, filter(lambda num: num % 2 == 0, numbers)))

print("mapped_and_filtered", doubled_evens_map_filter)

# ==================== List Compressions (inline for loops that creates a list) ===============

doubled_comprehension = [num * 2 for num in numbers]
print("Doubled Comprehension", doubled_comprehension)

evens = [num for num in numbers if num % 2 == 0]
print("Evens Comprehension", evens)

doubled_evens_comprehension = [num * 2 for num in numbers if num % 2 == 0]
print("Doubled Evens Comprehension", doubled_evens_comprehension)

# [expression for item in list condition]

# ================ Real world data processing with comprehensions =============

employees = [
    {'name': 'Alice Johnson', 'job': 'Developer', 'salary': 75000},
    {'name': 'Bob Smith', 'job': 'Designer', 'salary': 65000},
    {'name': 'Carol Davis', 'job': 'Manager', 'salary': 85000},
    {'name': 'David Wilson', 'job': 'Analyst', 'salary': 55000},
    {'name': 'Emma Brown', 'job': 'Developer', 'salary': 82000}
]

developer_raise = [{'name': employee['name'], 'job':employee['job'], "salary":employee['salary']*1.1} for employee in employees if employee['job'] == 'Developer']
print(developer_raise)

# Show our high earning develops
high_earners = [employee for employee in employees if employee['salary'] >=75000 and employee['job'] == 'Developer']
print(high_earners)




# Efficiency

# List Comprehensions
# User Defined functions
# Map and Filter