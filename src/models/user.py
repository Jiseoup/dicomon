from typing import List
from sqlalchemy import BigInteger, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin


class User(Base, TimestampMixin):
    """User model."""
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    discord_id: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
        index=True
    )
    username: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    coin: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0 # TODO: 코인 초기 자급량 설정 필요
    )

    # Relationships.
    dicomons: Mapped[List['Dicomon']] = relationship(
        'Dicomon',
        back_populates='user',
        cascade='all, delete-orphan'
    )
