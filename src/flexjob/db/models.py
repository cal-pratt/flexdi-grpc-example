import uuid

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column


class Base(DeclarativeBase):
    pass


class FlexJob(Base):
    __tablename__ = "flexjobs"

    job_id: MappedColumn[str] = mapped_column(
        String(), default=lambda: str(uuid.uuid4()), primary_key=True
    )
    instance: MappedColumn[str] = mapped_column(String, nullable=False)
