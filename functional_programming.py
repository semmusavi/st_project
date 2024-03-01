from functools import reduce
# this is functional programming file
# Higher-Order Function
def process_data(books, func):
  return list(map(func, books))

# Side-Effect Free Function
def get_price(book):
  return book['price']

# Closure
def make_genre_filter(genre):
  def genre_filter(book):
    return book['genre'] == genre
  return genre_filter

# Final Data Structure
books = [
    {'title': 'The Great Gatsby', 'price': 10, 'genre': 'Fiction'},
    {'title': 'A Brief History of Time', 'price': 15, 'genre': 'Science'},
    {'title': 'To Kill a Mockingbird', 'price': 20, 'genre': 'Fiction'},
]

# Functions as Parameters and Return Values
filter_fiction = make_genre_filter('Fiction')
fiction_books = list(filter(filter_fiction, books))
fiction_total = reduce(lambda x, y: x + y, process_data(fiction_books, get_price))

print("Total cost of Fiction books: ", fiction_total)
