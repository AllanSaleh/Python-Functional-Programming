# Map is a higher order function that will do something to each item in a list, and produce the modified list

numbers = [1,2,3,4,5]

# Standard approach
def double_nums(alist):
  output = []
  for num in alist:
    output.append(num*2)
  
  return output

doubled_nums = double_nums(numbers)
print("original", numbers)
print("doubled", doubled_nums)

# The Map approach with lambdas
# map(function, list)

new_double_nums = list(map(lambda num: num * 2, numbers))
print(new_double_nums)


# Regular way
def my_func(num):
  return num * 2

regular_double_nums = list(map(my_func, numbers))
print("regular", regular_double_nums)


# ==================== Processing more complicated data ===============

users = [
  {'name': 'Petter Cottontail', 'email':'PCOTTON@EMAIL.COM'},
  {'name': 'Tony start', 'email':'TONYS@EMAIL.COM'},
  {'name': 'peter quil', 'email':'PQUIL@EMAIL.COM'}
]

# Create a function to normalize our users
# .title() case their names
# .lower() case their emails
# Give them a username, lowercase name, names separated by underscore

def normalize_user(user):
  return {
    'name': user['name'].title(), #Title case the user's name and restore it in a new dictionary
    'email': user['email'].lower(),
    'username': user['name'].lower().replace(" ","_") #replace takes 2 arguments, (what we replace, what we replace it with)
  }
# User processed functions are better for large scale processing
processed_users = list(map(normalize_user, users))
print(processed_users)

# Lambdas are good for simple processing
process_emails_only = list(map(lambda user: {"name": user['name'], 'email': user['email'].lower()}, users))

print("emails processed", process_emails_only)