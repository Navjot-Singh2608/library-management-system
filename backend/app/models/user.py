from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import DateTime, Enum as SQLEnum, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class UserRole(str, PyEnum):
    MEMBER = "MEMBER"
    LIBRARIAN = "LIBRARIAN"
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name="user_role"), default=UserRole.MEMBER, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
