from sqlalchemy import Column, Integer, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    completion_percentage = Column(Float, nullable=False, default=0)

    user = relationship("User", back_populates="progress")
    note = relationship("Note")

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "note_id",
            name="unique_user_note_progress",
        ),
    )
