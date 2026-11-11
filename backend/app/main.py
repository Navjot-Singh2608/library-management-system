from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.user import User  # noqa: F401  (import so the table is registered)
from app.routers import auth

# Temporary: creates the tables that don't exist yet. Alembic will replace this later.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management System")

app.include_router(auth.router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
