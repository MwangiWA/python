# Base class: Book
class Book:
    def __init__(self, title, author, pages):
        # Constructor: sets the common attributes for all books
        self.title = title
        self.author = author
        self._pages = pages  # Protected attribute (by convention, not directly accessed outside)

    def display_info(self):
        # Prints the basic book information
        print(f"📘 '{self.title}' by {self.author} - {self._pages} pages")

    def read(self):
        # Simulates reading the book
        print(f"You're now reading '{self.title}' 📖")

# Subclass: EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        # Initialize parent class (Book) using super()
        super().__init__(title, author, pages)
        self.file_size = file_size  # Specific to EBooks

    def download(self):
        # Simulates downloading an ebook
        print(f"Downloading '{self.title}' ({self.file_size}MB)... 💾")

# Subclass: AudioBook inherits from Book
class AudioBook(Book):
    def __init__(self, title, author, pages, duration):
        # Initialize parent class (Book)
        super().__init__(title, author, pages)
        self.duration = duration  # Specific to audiobooks

    def play(self):
        # Simulates playing the audiobook
        print(f"Playing audiobook '{self.title}' 🎧 Duration: {self.duration} minutes")

# ----- Interactive Section -----
print("📚 Create your Book!")  # Title for user interface
book_type = input("Choose type (EBook or AudioBook): ").strip().lower()  # Ask user for book type

# Ask user for common book details
title = input("Enter book title: ")
author = input("Enter author name: ")
pages = int(input("Enter number of pages: "))

# Check the book type and create the appropriate object
if book_type == "ebook":
    size = float(input("Enter file size (MB): "))  # EBook-specific input
    book = EBook(title, author, pages, size)       # Create EBook object
    book.display_info()
    book.download()
    book.read()

elif book_type == "audiobook":
    duration = int(input("Enter duration (in minutes): "))  # AudioBook-specific input
    book = AudioBook(title, author, pages, duration)        # Create AudioBook object
    book.display_info()
    book.play()
    book.read()

else:
    print("Unknown book type. Please choose either 'EBook' or 'AudioBook'.")  # Error handling
