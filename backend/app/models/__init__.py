# Import every model here so SQLAlchemy (and Alembic) know about all tables.
from app.models.book import Book, book_authors, book_categories
from app.models.author import Author
from app.models.category import Category

__all__ = ["Book", "Author", "Category", "book_authors", "book_categories"]
