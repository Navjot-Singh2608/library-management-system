# Library Management System

A backend REST API for running a library: managing books, authors and categories, registering members, tracking borrowing and returns, and calculating fines for overdue books. Built with **FastAPI** and **PostgreSQL**, with JWT authentication and role-based access for members, librarians and admins.

> **Status:** in active development. User registration and login are complete; the books, loans and fines modules are being built next. See the [roadmap](#roadmap).

---

## Features

| Feature | Status |
|---|---|
| User registration with validation (email format, password rules, password confirmation) | ✅ Done |
| Login with JWT access tokens | ✅ Done |
| Secure password hashing (Argon2) | ✅ Done |
| Role-based access: Member, Librarian, Admin | 🚧 In progress |
| Manage books, authors and categories (CRUD) | 🚧 In progress |
| Search and filter books with pagination | 📋 Planned |
| Borrow and return books with due-date tracking | 📋 Planned |
| Automatic fines for overdue returns | 📋 Planned |
| Reports: popular books, overdue loans, active members | 📋 Planned |
| React frontend | 📋 Planned |

---

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python 3.12 |
| API framework | FastAPI |
| Validation | Pydantic v2 |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.x |
| Migrations | Alembic |
| Authentication | JWT (PyJWT), Argon2 password hashing (pwdlib) |
| Configuration | pydantic-settings with `.env` files |
| Testing | pytest |

---

## Architecture

The backend follows a layered design so each part has a single responsibility:

```mermaid
flowchart LR
    Client["Client<br/>(Swagger UI / React)"] -->|JSON over HTTP + JWT| Routers
    subgraph API["FastAPI application"]
        Routers["Routers<br/>HTTP endpoints"] --> Services["Services<br/>business rules"]
        Services --> Models["Models<br/>SQLAlchemy"]
    end
    Models --> DB[("PostgreSQL")]
```

- **Routers** receive requests and return responses. They contain no business logic.
- **Services** hold the business rules, for example "a member can borrow at most 3 books."
- **Schemas** (Pydantic) validate incoming data and control what is returned, so sensitive fields like password hashes never leave the API.
- **Models** (SQLAlchemy) define the database tables.

### Data model

```mermaid
erDiagram
    USERS ||--o{ LOANS : borrows
    BOOKS ||--o{ LOANS : "is borrowed in"
    LOANS ||--o| FINES : "may incur"
    BOOKS }o--o{ AUTHORS : "written by"
    BOOKS }o--o{ CATEGORIES : "belongs to"
```

A full design document with the architecture, database schema and borrow/return flow is in [`docs/`](docs/).

---

## Project Structure

```
library-management-system/
├── backend/
│   ├── app/
│   │   ├── main.py            # creates the app and registers routers
│   │   ├── dependencies.py    # shared dependencies (current user, role checks)
│   │   ├── core/              # settings and security (hashing, JWT)
│   │   ├── db/                # database engine and session
│   │   ├── models/            # SQLAlchemy tables
│   │   ├── schemas/           # Pydantic request/response models
│   │   ├── services/          # business logic
│   │   └── routers/           # API endpoints
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
├── docs/                      # design documentation
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL 13+

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/library-management-system.git
cd library-management-system/backend

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env           # then edit .env with your database password and a secret key
```

Create the database in PostgreSQL:

```sql
CREATE DATABASE library_db;
```

### Run

```bash
uvicorn app.main:app --reload
```

Then open the interactive API documentation at **http://127.0.0.1:8000/docs**.

### Environment variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string, e.g. `postgresql+psycopg://postgres:password@localhost:5432/library_db` |
| `SECRET_KEY` | Secret used to sign JWT tokens. Generate one with `python -c "import secrets; print(secrets.token_hex(32))"` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime in minutes (default: 30) |

---

## API Endpoints

All endpoints are served under `/api/v1`.

| Method | Endpoint | Description | Status |
|---|---|---|---|
| POST | `/auth/register` | Create a new member account | ✅ |
| POST | `/auth/login` | Log in and receive a JWT access token | ✅ |
| GET | `/books` | List books with search, filters and pagination | 📋 |
| POST | `/books` | Add a book (librarian only) | 📋 |
| POST | `/loans` | Borrow a book | 📋 |
| POST | `/loans/{id}/return` | Return a book | 📋 |

### Example: register

```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "username": "navjot",
  "email": "navjot@example.com",
  "password": "secret123",
  "confirm_password": "secret123"
}
```

Response `201 Created`:

```json
{
  "id": 1,
  "username": "navjot",
  "email": "navjot@example.com",
  "role": "MEMBER",
  "created_at": "2026-11-11T10:30:00Z"
}
```

---

## Key Design Decisions

- **Passwords are never stored.** Only an Argon2 hash is saved, and API responses never include it.
- **Same error for wrong username or wrong password**, so the login endpoint doesn't reveal which usernames exist.
- **Separate request and response schemas**, so clients can't set fields like `id` or `role`, and internal fields stay private.
- **Database-generated integer IDs** (PostgreSQL auto-increment), guaranteed unique even with multiple servers.
- **Overdue status is calculated, not stored**, because it changes with time on its own and a stored value would go stale.
- **Safe borrowing under concurrency:** the "copies available" check and update will run as a single atomic database operation, so two members can never borrow the last copy at the same time.

---

## Roadmap

- [x] Project structure and configuration
- [x] User registration and login with JWT
- [ ] Role-based route protection
- [ ] Books, authors and categories CRUD
- [ ] Search, filtering and pagination
- [ ] Borrow and return with business rules
- [ ] Fines for overdue returns
- [ ] Alembic migrations
- [ ] Automated tests
- [ ] Docker Compose setup
- [ ] React frontend

---

## Author

**Navjot Singh**
