from app.db.database import Base, engine
from app.models import (
    User,
    Level,
    Semester,
    Module,
    Topic,
    Note,
    Quiz,
    Question,
    PastPaper,
    Bookmark,
    Progress,
)

Base.metadata.create_all(bind=engine)

print("All database tables created successfully")
