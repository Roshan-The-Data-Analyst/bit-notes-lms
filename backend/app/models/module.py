from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    semester_id = Column(Integer, ForeignKey("semesters.id"), nullable=False)
    code = Column(String(50), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    credits = Column(Integer, nullable=True)
    image_url = Column(String(500), nullable=True)

    semester = relationship("Semester", back_populates="modules")
    topics = relationship(
        "Topic",
        back_populates="module",
        cascade="all, delete-orphan",
    )
    past_papers = relationship(
        "PastPaper",
        back_populates="module",
        cascade="all, delete-orphan",
    )
