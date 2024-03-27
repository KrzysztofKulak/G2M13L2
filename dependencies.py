from fastapi import Depends

from src.database.db import get_db
from src.repository.notes import NotesRepository


def get_notes_repository(db=Depends(get_db)):
    return NotesRepository(db)


