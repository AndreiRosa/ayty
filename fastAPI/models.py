from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Call(Base):
    __tablename__ = "call"

    id_call = Column(Integer, primary_key=True, index=True, nullable=False)
    extension = Column(String(4), nullable=False)
    nu_ddd = Column(String(2), nullable=False)
    nu_phone = Column(String(9), nullable=False)
    dt_start = Column(Date, nullable=False)
    dt_answer = Column(Date, nullable=False)
    dt_finish = Column(Date, nullable=False)

    owner_id = Column(Integer, ForeignKey("extension.id"))
    owner = relationship("Extension", back_populates="call")


class Extent_event(Base):
    __tablename__ = "extent_event"

    id_extent_event = Column(Integer, primary_key=True, index=True)
    extension = Column(String(4), nullable=False)
    status = Column(String(9), nullable=False)
    dt_event = Column(Date, nullable=False)

    owner_id = Column(Integer, ForeignKey("extension.id"))
    owner = relationship("Extension", back_populates="extent_event")


class Extension(Base):
    __tablename__ = "extension"

    id_extension = Column(Integer, primary_key=True, index=True)
    extension = Column(String(4), nullable=False)
    nm_extension = Column(String(9), nullable=False)
    is_active = Column(Boolean, default=True)
    must_record = Column(Boolean, default=True)
    nm_transfer = Column(String(9), nullable=True)
    was_exported = Column(Boolean, default=True)
    call = relationship("Extension", back_populates="owner")
    extent_event = relationship("Extension", back_populates="owner")