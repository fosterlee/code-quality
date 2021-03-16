from datetime import date
from typing import List

from pydantic import BaseModel


class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: List[str]


song = Song(
    id=101,
    name="Bohemian Rhapsody",
    release="1975-31-31",
    genres=["Hard Rock", "Progressive Rock"],
)
print(song)
# id=101 name='Bohemian Rhapsody' release=datetime.date(1975, 10, 31)
# genres=['Hard Rock', 'Progressive Rock']
