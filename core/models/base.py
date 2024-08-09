from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    # __tablename__
    __abstract__ = True
