from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)

    user = relationship("User", back_populates="bookmarks")
    note = relationship("Note")

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "note_id",
            name="unique_user_note_bookmark",
        ),
    )
