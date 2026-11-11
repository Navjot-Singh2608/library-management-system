from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.book import book_authors

if TYPE_CHECKING:
    from app.models.book import Book


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), index=True)
    birth_year: Mapped[int | None] = mapped_column(Integer)

    books: Mapped[list["Book"]] = relationship(
        secondary=book_authors, back_populates="authors"
    )

    def __repr__(self) -> str:
        return f"<Author id={self.id} name={self.name!r}>"
