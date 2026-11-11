from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum as PyEnum

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey,
                        Enum as SQLEnum, Integer, Numeric, String, Table, Text)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.book import Book
from db.database import Base


class Loans(Base):

    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True)
    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"), nullable=False, index=True)
    borrowed_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True))
    due_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True))
    return_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True))

    book: Mapped["Book"] = relationship(back_populates="loans")

    status: ACTIVE | RETURN
