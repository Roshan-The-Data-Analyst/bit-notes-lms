from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:password@localhost:5432/bit_notes"

engine = create_engine(DATABASE_URL)