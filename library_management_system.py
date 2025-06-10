class Library_T:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def remove_book(self, identifier):
        for book in self.books:
            if (book.title.lower() == identifier.lower() or
                book.author.lower() == identifier.lower() or
                book.isbn == identifier):
                self.books.remove(book)
                print(f"Removed book: {book}")
                return
        print(f"Book '{identifier}' not found.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found.")
        return None

    def search_books(self, keyword):
        results = []
        keyword = keyword.lower()
        for book in self.books:
            if (keyword in book.title.lower() or
                keyword in book.author.lower() or
                keyword in book.isbn):
                results.append(book)
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found for '{keyword}'.")

    def total_books(self):
        print(f"Total number of books: {len(self.books)}")
        return len(self.books)

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)

class Library:
    def __init__(self):
        self.books = []
        self.type = []
    def add_book(self,book,type):
        self.books.append(book)
        self.type.append(type)
        print(f"Added book: {book} ({type})")
    @property
    def status(self):
        print(f"Total books: {len(self.books)}")
Library().add_book("GOT","war")
Library().status
