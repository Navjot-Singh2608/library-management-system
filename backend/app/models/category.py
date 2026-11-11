from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.book import book_categories

if TYPE_CHECKING:
    from app.models.book import Book


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    books: Mapped[list["Book"]] = relationship(
        secondary=book_categories, back_populates="categories"
    )

    def __repr__(self) -> str:
        return f"<Category id={self.id} name={self.name!r}>"
