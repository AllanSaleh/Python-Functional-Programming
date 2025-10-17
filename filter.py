# Filter is a higher order function that takes in a list
# Evaluates the contents individually and creates a new list of items
# Based on who met a certain criteria/condition

# Standard way
numbers = [1,2,3,4,5]

# Write a function that took in a list of numbers an returned only evens

def only_evens(nums):
  output = [] #This list I add to when an item passes my check
  for num in nums:
    if num % 2 == 0: # if I can divide this number by 2 and the remainder is 0
      output.append(num)
  return output

print(only_evens(numbers))


# Filter
# syntax
# filter(function, list)
# If True - item makes it to the output list
# If False - item gets filtered out

# Filtering with lambda

evens = list(filter(lambda num: num % 2 == 0, numbers))

print("Evens", evens)

# Filtering with a user defined function

def is_even(num):
  return num % 2 == 0

ud_evens = list(filter(is_even, numbers))
print("user defined evens", ud_evens)


# =============== Filter real data ===================

transactions = [
  {'id': 1, 'amount':100.0, 'type':'credit', 'valid': False},
  {'id': 2, 'amount':-50.0, 'type':'credit', 'valid': False},
  {'id': 3, 'amount':200.0, 'type':'credit', 'valid': True},
  {'id': 4, 'amount':10.0, 'type':'debit', 'valid': False},
  {'id': 5, 'amount':70.0, 'type':'debit', 'valid': True},
]

# Filter by valid transaction

valid_transaction = list(filter(lambda transaction: transaction['valid'], transactions))
print('Valid transactions', valid_transaction)

debit_transactions = list(filter(lambda transaction: transaction['type'] == 'debit', transactions))
print('Debit transactions', debit_transactions)

high_credit_transaction = list(filter(lambda transaction: transaction['amount'] >= 100 and transaction['type'] == 'credit' and transaction['valid'], transactions))
print('Hight Credit transactions', high_credit_transaction)
