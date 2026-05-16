from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.user import User
from app.models.conversation import Conversation
from app.schemas.conversation import ConversationCreate, ConversationResponse
from app.routers.auth import get_current_user

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.get("/", response_model=List[ConversationResponse])
def get_conversations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    convs = (
        db.query(Conversation)
        .filter(
            (Conversation.user1_id == current_user.id)
            | (Conversation.user2_id == current_user.id)
        )
        .all()
    )
    return convs


@router.post("/", response_model=ConversationResponse)
def create_conversation(
    conv: ConversationCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Must be participant
    if conv.user1_id != current_user.id and conv.user2_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not participant in this conversation"
        )

    # Normalise order (smaller ID first)
    user1, user2 = conv.user1_id, conv.user2_id
    if user1 > user2:
        user1, user2 = user2, user1

    # Check if conversation already exists
    existing = (
        db.query(Conversation)
        .filter(Conversation.user1_id == user1, Conversation.user2_id == user2)
        .first()
    )
    if existing:
        return existing

    new_conv = Conversation(user1_id=user1, user2_id=user2)
    db.add(new_conv)
    db.commit()
    db.refresh(new_conv)
    return new_conv
