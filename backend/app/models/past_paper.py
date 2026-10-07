from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class PastPaper(Base):
    __tablename__ = "past_papers"

    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    title = Column(String(200), nullable=False)
    year = Column(Integer, nullable=True)
    semester = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    pdf_url = Column(String(500), nullable=False)

    module = relationship("Module", back_populates="past_papers")
