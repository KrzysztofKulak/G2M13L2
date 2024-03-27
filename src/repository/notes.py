from sqlalchemy.orm import Session

from src.database.models import Note, Tag
from src.repository.abstract import AbstractNotesRepository
from src.schemas import NoteIn, NoteStatusUpdate, UserOut, NoteOut

class NotesMongoRepository(AbstractNotesRepository):
    ...

class NotesRepository(AbstractNotesRepository):
    def __init__(self, db: Session):
        self._db = db
    
    async def get_notes(self, skip: int, limit: int, user: UserOut) -> list[NoteOut]:
        return self._db.query(Note).filter(Note.user_id == user.id).offset(skip).limit(limit).all()

    async def get_note(self, note_id: int, user: UserOut) -> NoteOut:
        return self._db.query(Note).filter(Note.id == note_id, Note.user_id == user.id).first()

    async def create_note(self, body: NoteIn, user: UserOut) -> NoteOut:
        tags = self._db.query(Tag).filter(Tag.id.in_(body.tags), Tag.user_id == user.id).all()
        note = Note(title=body.title, description=body.description, tags=tags, user_id=user.id)
        self._db.add(note)
        self._db.commit()
        self._db.refresh(note)
        return note

    async def remove_note(self, note_id: int, user: UserOut) -> NoteOut | None:
        note = self._db.query(Note).filter(Note.id == note_id, Note.user_id == user.id).first()
        if note:
            self._db.delete(note)
            self._db.commit()
        return note

    async def update_note(self, note_id: int, body: NoteIn, user: UserOut) -> NoteOut | None:
        note = self._db.query(Note).filter(Note.id == note_id, Note.user_id == user.id).first()
        if note:
            tags = self._db.query(Tag).filter(Tag.id.in_(body.tags)).all()
            note.title = body.title
            note.description = body.description
            note.done = body.done
            note.tags = tags
            self._db.commit()
        return note

    async def update_status_note(self, note_id: int, body: NoteStatusUpdate, user: UserOut) -> NoteOut | None:
        note = self._db.query(Note).filter(Note.id == note_id, Note.user_id == user.id).first()
        if note:
            note.done = body.done
            self._db.commit()
        return note
