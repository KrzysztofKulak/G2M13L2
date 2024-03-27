from typing import List

from sqlalchemy.orm import Session

from src.database.models import Tag
from src.schemas import TagIn, UserOut


async def get_tags(skip: int, limit: int, user: UserOut, db: Session) -> List[Tag]:
    return db.query(Tag).filter(Tag.user_id == user.id).offset(skip).limit(limit).all()


async def get_tag(tag_id: int, user: UserOut, db: Session) -> Tag:
    return db.query(Tag).filter(Tag.id == tag_id, Tag.user_id == user.id).first()


async def create_tag(body: TagIn, user: UserOut, db: Session) -> Tag:
    tag = Tag(name=body.name, user_id=user.id)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


async def update_tag(tag_id: int, body: TagIn, user: UserOut, db: Session) -> Tag | None:
    tag = db.query(Tag).filter(Tag.id == tag_id, Tag.user_id == user.id).first()
    if tag:
        tag.name = body.name
        db.commit()
    return tag


async def remove_tag(tag_id: int, user: UserOut, db: Session) -> Tag | None:
    tag = db.query(Tag).filter(Tag.id == tag_id, Tag.user_id == user.id).first()
    if tag:
        db.delete(tag)
        db.commit()
    return tag
