from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

CURRENT_YEAR = date.today().year


# ================= BOOKS =================
class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=2000)
    published_year: int = Field(ge=1450, le=CURRENT_YEAR)
    total_copies: int = Field(default=1, ge=1)

    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        v = v.strip().title()
        if not v:
            raise ValueError("Please enter the title")
        else:
            return v


class addBook(BookBase):
    pass


class BookUpdate(BookBase):
    id: int


class AuthorBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    birth_year: int = Field(ge=1000, le=CURRENT_YEAR)


class AddAuthor(AuthorBase):
    pass


class BookAuthorCreate(BaseModel):
    author_id: int
