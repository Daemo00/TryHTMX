"""Manage the DB."""
from sqlmodel import create_engine
from sqlmodel.main import SQLModel
from sqlmodel.orm.session import Session
from models.hero import populate as hero_populate

engine = create_engine("sqlite://database.db")
SQLModel.metadata.create_all(engine)


def _populate_records():
    """Get records for `populate`."""
    return hero_populate()


def populate():
    """Create data in DB."""
    populate_records = _populate_records()

    with Session(engine) as session:
        for record in populate_records:
            session.add(record)
        session.commit()
