### Self Parameter ###

class Dog:
    def __init__(self, name):
        # Here, 'self.name' is an attribute attached to this Dog instance
        self.name = name

    def bark(self):
        # 'self' refers to the instance on which bark() is called
        print(f"{self.name} says woof!")

class Cat:
    def __init__(current_object, name):
        # You don't need to use self but it's strongly suggested because ✨convention✨
        current_object.name = name

    def meow(current_object):
        # 'self' refers to the instance on which meow() is called
        print(f"{current_object.name} says meow!")


# Create a Dog instance
my_dog = Dog("Buddy")
# Call the bark method on the instance
my_dog.bark()  # Output: Buddy says woof!
# Create a Cat instance
my_cat = Cat("Mr. Whiskers IV")
# Call the meow method on the instance
my_cat.meow()

### Exercise ###

# Book class
class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = False


# Book Collection class
class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("List must contain only Book instances")

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only book instances can be added")
        self.books.append(book)
        print(f"{book.name} has been added to the list")

    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = True
                print(f"{book_name} has been marked as read")
                return

        print("Book not found in collection")

    def list_books(self):
        for book in self.books:
            # status = None
            # if book.read:
            #     status = "Read"
            # else:
            #     status = "Unread"

            status = "Read" if book.read else "Unread"

            print(f"Title: {book.name} , Author: {book.author}, Status: {status}")


# Instances of books
harry_potter = Book("Harry Potter", "JK Rowling", 2000)
got = Book("Game of thrones", "George Martin", 2000)

# Instance of book collection
my_collection = BookCollection()

# Calling methods on the book collection
my_collection.add_book(harry_potter)
my_collection.add_book(got)

my_collection.mark_as_read("Harry Potter")
my_collection.list_books()
Collapse

