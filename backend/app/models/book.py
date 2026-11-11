from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum as PyEnum

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey,
                        Enum as SQLEnum, Integer, Numeric, String, Table, Text)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.loan import Loans
from db.database import Base


class UserRole(str, PyEnum):
    MEMBER = "MEMBER"
    LIBRARIAN = "LIBRARIAN"
    ADMIN = "ADMIN"


class LoanStatus(str, PyEnum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    published_year: Mapped[int] = mapped_column(Integer, nullable=False)
    total_copies: Mapped[int] = mapped_column(Integer, nullable=False)
    available_copies: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True))
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True))

    loans: Mapped[list["Loans"]] = relationship(back_populates="books")
    User: Mapped[list["Book"]] = relationship(back_populates="users")


book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("author_id", ForeignKey("authors.id"), primary_key=True),
)
