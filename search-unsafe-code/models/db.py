from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SeverityLevel(Base):
    __tablename__ = "severity_levels"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    vulnerabilities = relationship("Vulnerability", back_populates="severity")

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    class_id = Column(String, nullable=False)
    keyword = Column(String, nullable=False)
    severity_id = Column(Integer, ForeignKey("severity_levels.id"))
    severity = relationship("SeverityLevel", back_populates="vulnerabilities")