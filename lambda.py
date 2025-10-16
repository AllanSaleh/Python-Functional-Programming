# Basic function syntax
# def name_of_func(parameters):
#   #code block

def calculate_tax(price):
  # Calculate 7% sales tax
  tax = price * .07
  return tax

print(f"{calculate_tax(136):.2f}")

# Lambda Functions aka Anonymous Functions
# Syntax
# lambda parameters: expression who value is returned

lambda price: price *.07 #Anonymous function because it has no name

calculate_tax = lambda price: price *.07

print(calculate_tax(15))


#  ============ Sorting Keys with Lambda Functions ================

products = [
  {'name': 'laptop', 'price': 999.99},
  {'name': 'mouse', 'price': 64.99},
  {'name': 'keyboard', 'price': 129.99},
]


# print(sorted(products))

# create a sorting to target specific fields for individual pieces of data

print(sorted(products, key=lambda product: product["price"], reverse=True))


def func_for_sort(product):
  return product["name"]

print(sorted(products, key=func_for_sort, reverse=True))



students = ["Lanre Akinbo", "Troy Wenzel", "Joe Burgess"]

print(sorted(students))


# name = "Lanre Akinbo"
# print(name.split()[1])

print("Sorting by last name (Target the last name with sort key)")
print(sorted(students, key=lambda student: student.split(" ")[1]))

# =================== Lambdas as Conditionals (inline if statements) aka ternary operator

grade = 80

if grade >=90:
  print("A")
elif grade >=80:
  print('B')
else:
  print('Fail')


# Inline lambda conditional

assign_letter_grade = lambda grade: 'A' if grade >= 90 else 'B' if grade >= 80 else 'C'

print("The grade is:", assign_letter_grade(95))

# ============== 2 param for lambdas

add = lambda a, b: a + b
print(add(5,7))