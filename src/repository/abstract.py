import abc

from src.schemas import UserOut, NoteOut, NoteIn, NoteStatusUpdate


class AbstractNotesRepository(abc.ABC):
    @abc.abstractmethod
    async def get_notes(self, skip: int, limit: int, user: UserOut) -> list[NoteOut]:
        ...

    @abc.abstractmethod
    async def get_note(self, note_id: int, user: UserOut) -> NoteOut:
        ...

    @abc.abstractmethod
    async def create_note(self, body: NoteIn, user: UserOut) -> NoteOut:
        ...

    @abc.abstractmethod
    async def remove_note(self, note_id: int, user: UserOut) -> NoteOut | None:
        ...

    @abc.abstractmethod
    async def update_note(self, note_id: int, body: NoteIn, user: UserOut) -> NoteOut | None:
        ...

    @abc.abstractmethod
    async def update_status_note(self, note_id: int, body: NoteStatusUpdate, user: UserOut) -> NoteOut | None:
        ...