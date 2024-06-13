"""Hero Model."""
from typing import Optional

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    """Hero Model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


def populate():
    """Populate the Hero table."""
    hero_1 = Hero(
        name="SuperPippo",
        secret_name="Pippo",  # nosec: B106:hardcoded_password_funcarg
    )
    hero_2 = Hero(
        name="SuperPippa",
        secret_name="Pippa",  # nosec: B106:hardcoded_password_funcar
    )
    return hero_1, hero_2
