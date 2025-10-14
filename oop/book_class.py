class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor to initialize book details."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """Destructor to indicate when a book object is deleted."""
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
