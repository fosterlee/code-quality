from datetime import date
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()


class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: List[str]

    @validator("genres")
    def no_duplicates_in_genre(cls, v):
        if len(set(v)) != len(v):
            raise ValueError("No duplicates allowed in genre.")
        return v


song = Song(
    id=101,
    name="Bohemian Rhapsody",
    release="1975-10-31",
    genres=[
        "Hard Rock",
        "Progressive Rock",
    ],
)


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
