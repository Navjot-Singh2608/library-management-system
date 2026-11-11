from pydantic import Base64Bytes
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey,
                        Enum as SQLEnum, Integer, Numeric, String, Table, Text)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.loan import Loans
from db.database import Base
from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum as PyEnum


class Fine(Base):
    __tablename__ = "fines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    loan_id: Mapped[int] = mapped_column(
        ForeignKey("loans.id"), unique=True, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    is_paid: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)
    paid_on: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True)
