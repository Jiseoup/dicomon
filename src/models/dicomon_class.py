import enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import BigInteger, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin


class MainClass(str, enum.Enum):
    """Dicomon main class types."""
    RABBIT = 'rabbit'
    FOX = 'fox'
    BEAR = 'bear'
    EAGLE = 'eagle'
    DEER = 'deer'


class SubClass(str, enum.Enum):
    """Dicomon sub class types."""
    # Rabbit
    NINJA = 'ninja'
    TIME = 'time'
    THUNDER = 'thunder'

    # Fox
    FIRE = 'fire'
    ILLUSION = 'illusion'
    MAGICIAN = 'magician'

    # Bear
    BERSERKER = 'berserker'
    GUARDIAN = 'guardian'

    # Eagle
    LAW = 'law'
    ARCHER = 'archer'

    # Deer
    LIFE = 'life'
    SPIRIT = 'spirit'


class DicomonClass(Base, TimestampMixin):
    """DicomonClass model representing dicomon species information."""
    __tablename__ = 'dicomon_class'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    main_class: Mapped[MainClass] = mapped_column(
        SQLEnum(MainClass),
        nullable=False
    )
    sub_class: Mapped[SubClass | None] = mapped_column(
        SQLEnum(SubClass),
        nullable=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    level: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    image_url: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
