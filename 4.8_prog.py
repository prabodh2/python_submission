class LibraryItem:
    def __init__(self, title, item_id, is_available=True):
        self.title = title
        self.item_id = item_id
        self.is_available = is_available

    def display_info(self):
        print(f"Title: {self.title}, Item ID: {self.item_id}")
        status = "Available" if self.is_available else "Checked Out"
        print(f"Status: {status}")

    def check_out(self):
        if self.is_available:
            print(f"{self.title} has been checked out.")
            self.is_available = False
        else:
            print(f"Sorry, {self.title} is already checked out.")

    def check_in(self):
        if not self.is_available:
            print(f"{self.title} has been checked in.")
            self.is_available = True
        else:
            print(f"Error: {self.title} is already available.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages):
        super().__init__(title, item_id)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}, Pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}, Duration: {self.duration} minutes")


class Journal(LibraryItem):
    def __init__(self, title, item_id, publisher, publication_year):
        super().__init__(title, item_id)
        self.publisher = publisher
        self.publication_year = publication_year

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}, Year: {self.publication_year}")


# Example usage:
def main():
    # Create instances of Book, DVD, and Journal
    book = Book("Python Programming", "B001", "John Doe", 300)
    dvd = DVD("Introduction to Python", "D001", "Jane Smith", 120)
    journal = Journal("Science Journal", "J001", "Science Publications", 2023)

    # Display information and perform check-out/check-in operations
    print("\nDisplay Information:")
    book.display_info()
    dvd.display_info()
    journal.display_info()

    print("\nCheck Out Operations:")
    book.check_out()
    dvd.check_out()
    journal.check_out()

    print("\nCheck In Operations:")
    book.check_in()
    dvd.check_in()
    journal.check_in()

if __name__ == "__main__":
    main()
