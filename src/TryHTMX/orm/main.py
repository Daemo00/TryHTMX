"""Manage the DB."""
from sqlmodel import create_engine
from sqlmodel.main import SQLModel
from sqlmodel.orm.session import Session
from .models.hero import populate as hero_populate

DB_CONN = "sqlite:///db.sqlite3"


def get_db():
    """Database engine."""
    engine = create_engine(DB_CONN)
    SQLModel.metadata.create_all(engine)
    return engine


def add_records(db, records):
    """Insert `records` in `db`."""
    with Session(db) as session:
        for record in records:
            session.add(record)
        session.commit()


def _populate_records():
    """Get records for `populate`."""
    return hero_populate()


def populate():
    """Create data in DB."""
    populate_records = _populate_records()
    add_records(get_db(), populate_records)
