"""Manage the DB."""
from sqlmodel import create_engine
from sqlmodel.main import SQLModel
from sqlmodel.orm.session import Session


def populate():
    """Create records."""
    return []


engine = create_engine("sqlite://database.db")
SQLModel.metadata.create_all(engine)

records = populate()

with Session(engine) as session:
    for record in records:
        session.add(record)
    session.commit()
