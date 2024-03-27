from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi_limiter.depends import RateLimiter

from dependencies import get_notes_repository
from src.repository.abstract import AbstractNotesRepository
from src.schemas import NoteIn, NoteStatusUpdate, NoteOut, UserOut
from src.services.auth import auth_service

router = APIRouter(prefix='/notes', tags=["notes"])


@router.get("/", response_model=List[NoteOut], description='No more than 10 requests per minute', dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_notes(skip: int = 0, limit: int = 100,
                     repository_notes: AbstractNotesRepository = Depends(get_notes_repository),
                     current_user: UserOut = Depends(auth_service.get_current_user)):
    notes = await repository_notes.get_notes(skip, limit, current_user)
    return notes


@router.get("/{note_id}", response_model=NoteOut)
async def read_note(note_id: int, repository_notes: AbstractNotesRepository = Depends(get_notes_repository),
                    current_user: UserOut = Depends(auth_service.get_current_user)):
    note = await repository_notes.get_note(note_id, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
async def create_note(body: NoteIn, repository_notes: AbstractNotesRepository = Depends(get_notes_repository),
                      current_user: UserOut = Depends(auth_service.get_current_user)
                      ):
    return await repository_notes.create_note(body, current_user)


@router.put("/{note_id}", response_model=NoteOut)
async def update_note(body: NoteIn, note_id: int,
                      repository_notes: AbstractNotesRepository = Depends(get_notes_repository),
                      current_user: UserOut = Depends(auth_service.get_current_user)):
    note = await repository_notes.update_note(note_id, body, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


@router.patch("/{note_id}", response_model=NoteOut)
async def update_status_note(body: NoteStatusUpdate, note_id: int,
                             repository_notes: AbstractNotesRepository = Depends(get_notes_repository),
                             current_user: UserOut = Depends(auth_service.get_current_user)):
    note = await repository_notes.update_status_note(note_id, body, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


@router.delete("/{note_id}", response_model=NoteOut)
async def remove_note(note_id: int, repository_notes: AbstractNotesRepository = Depends(get_notes_repository),
                      current_user: UserOut = Depends(auth_service.get_current_user)):
    note = await repository_notes.remove_note(note_id, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note
