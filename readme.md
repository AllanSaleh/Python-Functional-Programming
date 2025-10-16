# Lesson 4: Functional Programming - Student In-Class Practices

## In-Class Practice 1: Lambda Functions Practice

### Scenario
You're helping an online store manage their product inventory using Python. Your task is to use lambda functions to sort, categorize, and analyze product data efficiently.

### The Dataset
```python
products = [
    {'name': 'Wireless Headphones', 'price': 89.99, 'category': 'Electronics', 'stock': 45},
    {'name': 'Coffee Maker', 'price': 129.99, 'category': 'Appliances', 'stock': 12},
    {'name': 'Running Shoes', 'price': 79.99, 'category': 'Sports', 'stock': 23},
    {'name': 'Bluetooth Speaker', 'price': 59.99, 'category': 'Electronics', 'stock': 67},
    {'name': 'Yoga Mat', 'price': 24.99, 'category': 'Sports', 'stock': 8}
]
```

### Task 1: Basic Lambda Sorting

Use lambda functions to sort the product data in different ways:

```python
# TODO: Sort products by price (highest first)
by_price = sorted(products, key=# YOUR CODE HERE)

# TODO: Sort products by category, then by name alphabetically
by_category_name = sorted(products, key=# YOUR CODE HERE)

# Test your sorting
print("Most expensive:", by_price[0]['name'])
print("First alphabetically:", by_category_name[0]['name'])
```

### Task 2: Lambda Conditions

Create lambda functions that make decisions based on product data:

```python
# TODO: Create a lambda to determine price category
# - Price >= 100: 'Premium'
# - Price <= 50: 'Budget'  
# - Otherwise: 'Standard'
price_category = lambda price: # YOUR CODE HERE

# TODO: Create a lambda to check stock status
# - Stock <= 10: 'Low Stock'
# - Otherwise: 'In Stock'
stock_status = lambda stock: # YOUR CODE HERE

# Test your lambdas
print("Product Status Report:")
for product in products:
    category = price_category(product['price'])
    status = stock_status(product['stock'])
    print(f"{product['name']}: {category}, {status}")
```

---

## In-Class Practice 2: Map Function with Employee Salaries

### Scenario
The HR department needs your help calculating salary adjustments for all employees. You'll use the `map()` function with lambda expressions to process employee data efficiently.

### The Dataset
```python
employees = [
    {'name': 'Alice Johnson', 'job': 'Developer', 'salary': 75000},
    {'name': 'Bob Smith', 'job': 'Designer', 'salary': 65000},
    {'name': 'Carol Davis', 'job': 'Manager', 'salary': 85000},
    {'name': 'David Wilson', 'job': 'Analyst', 'salary': 55000},
    {'name': 'Emma Brown', 'job': 'Developer', 'salary': 72000}
]
```

### Task: Salary Increase Calculation

The company is giving all employees a 7% raise. Use `map()` with a lambda function to create updated employee records with the new salaries.

```python
# TODO: Use map() with lambda to create new employee dicts with 7% salary raise
updated_employees = list(map(# YOUR CODE HERE, employees))

# Test your result
print("Original employees:")
for emp in employees:
    print(f"  {emp['name']} ({emp['job']}): ${emp['salary']:,}")

print("\nAfter 7% raise:")
for emp in updated_employees:
    print(f"  {emp['name']} ({emp['job']}): ${emp['salary']:,.2f}")
```

## In-Class Practice 3: Filter Function with Book Data

### Scenario
You're helping a library system filter their book collection. You'll use the `filter()` function with lambda expressions to find books that meet specific criteria.

### The Dataset
```python
books = [
    {'title': 'Python Programming', 'pages': 320, 'rating': 4.5, 'available': True},
    {'title': 'Web Development', 'pages': 450, 'rating': 3.8, 'available': False},
    {'title': 'Data Science', 'pages': 280, 'rating': 4.9, 'available': True},
    {'title': 'Machine Learning', 'pages': 520, 'rating': 4.2, 'available': True},
    {'title': 'JavaScript Basics', 'pages': 180, 'rating': 3.5, 'available': False}
]
```

### Task: Find High-Quality Available Books

Find all books that are available AND have a rating of 4.0 or higher using `filter()` with a lambda function.

```python
# TODO: Use filter() with lambda to find available books with rating >= 4.0
quality_books = list(filter(# YOUR CODE HERE, books))

# Test your result
print("High-quality available books:")
for book in quality_books:
    print(f"  {book['title']} - Rating: {book['rating']}")
```
