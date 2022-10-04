import json
import pathlib

from book import Book

APP_DIR_PATH = pathlib.Path(__file__).parent.resolve()


class Library:
    """A representation of a library of books."""

    def __init__(self):
        """Init with archive and collection attribute."""
        self.archive = f"{APP_DIR_PATH}/archive.json"
        # Set collection attribute.
        self._get_collection()

    def _get_collection(self):
        """Set value of collection attribute by reading from a json file."""
        try:
            with open(self.archive, "r") as json_file:
                self.collection = json.load(json_file)
        except FileNotFoundError:
            with open(self.archive, "w") as json_file:
                self.collection = {}
                json.dump(self.collection, json_file)
            print("Archive not found. Creating a new empty archive json file.")

    def add_book(self):
        """Add a book to the library's collection."""
        book = Book()
        book.new_book()

        self._archive_collection()

    def _archive_book(self, book):
        """
        Update the collection and write to the archive.
        Expects the argument for the book parameter to be an instance of a book.
        """
        self.collection[book.title] = {
            "currently_reading": book.currently_reading,
            "total_pages": book.total_pages,
            "current_page": book.current_page,
            "chapters": book.chapters,
        }
        with open(self.archive, "w") as json_file:
            json.dump(self.collection, json_file)
