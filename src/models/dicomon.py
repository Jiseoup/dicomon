import enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, BigInteger, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin


class Status(str, enum.Enum):
    """Dicomon status types."""
    ALIVE = 'alive'
    INJURED = 'injured'
    DEAD = 'dead'


class Dicomon(Base, TimestampMixin):
    """Dicomon model."""
    __tablename__ = 'dicomon'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    class_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('dicomon_class.id', ondelete='RESTRICT'),
        nullable=False,
        index=True
    )
    level: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
        default=0
    )
    energy: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
        default=100
    )
    status: Mapped[Status] = mapped_column(
        SQLEnum(Status),
        nullable=False,
        default=Status.ALIVE
    )

    # Relationships.
    user: Mapped['User'] = relationship(
        'User',
        back_populates='dicomons'
    )
    dicomon_class: Mapped['DicomonClass'] = relationship(
        'DicomonClass'
    )
