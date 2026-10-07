# BIT Notes LMS Backend

FastAPI backend for the BIT Notes LMS project.

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL / Supabase
- Pydantic
- Uvicorn

## Setup

1. Create/activate the Python virtual environment.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Create `.env` from `.env.example`.
4. Put the Supabase `DATABASE_URL` in `.env`.
5. Create database tables:

   `python create_tables.py`

6. Start the API:

   `python -m uvicorn app.main:app --reload`

API documentation is available at `/docs`.

## Note

This package is a backend foundation so frontend development can continue independently. Authentication, full CRUD routes, file storage, and production migrations can be added later.
