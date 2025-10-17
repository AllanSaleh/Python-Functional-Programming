products = [
    {'name': 'Wireless Headphones', 'price': 89.99, 'category': 'Electronics', 'stock': 45},
    {'name': 'Coffee Maker', 'price': 129.99, 'category': 'Appliances', 'stock': 12},
    {'name': 'Running Shoes', 'price': 79.99, 'category': 'Sports', 'stock': 23},
    {'name': 'Bluetooth Speaker', 'price': 59.99, 'category': 'Electronics', 'stock': 67},
    {'name': 'Yoga Mat', 'price': 24.99, 'category': 'Sports', 'stock': 8}
]

# TODO: Sort products by price (highest first)
by_price = sorted(products, key=lambda product: product['price'], reverse=True)

# TODO: Sort products by category, then by name alphabetically
by_category_name = sorted(products, key=lambda product: (product['category'], product['name']))
# Test your sorting
print("Most expensive:", by_price[0]['name'])
print("First alphabetically:", by_category_name[0]['name'])