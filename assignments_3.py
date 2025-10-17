books = [
    {'title': 'Python Programming', 'pages': 320, 'rating': 4.5, 'available': True},
    {'title': 'Web Development', 'pages': 450, 'rating': 3.8, 'available': False},
    {'title': 'Data Science', 'pages': 280, 'rating': 4.9, 'available': True},
    {'title': 'Machine Learning', 'pages': 520, 'rating': 4.2, 'available': True},
    {'title': 'JavaScript Basics', 'pages': 180, 'rating': 3.5, 'available': False}
]

# TODO: Use filter() with lambda to find available books with rating >= 4.0
quality_books = list(filter(lambda book: book['available'] and book['rating']>= 4.0, books))

# Test your result
print("High-quality available books:")
for book in quality_books:
    print(f"  {book['title']} - Rating: {book['rating']}")