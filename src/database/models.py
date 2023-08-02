from datetime import date

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.database.db import Base


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    surname: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    number: Mapped[str] = mapped_column(String(150), index=True, unique=True)
    bd_date: Mapped[date] = mapped_column(Date, index=True)
    additional_data: Mapped[str] = mapped_column(String(255))
