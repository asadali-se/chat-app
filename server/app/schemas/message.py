from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageBase(BaseModel):
    content: str
    conversation_id: int


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    sender_id: int
    message_type: str
    media_url: Optional[str] = None
    is_delivered: bool
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
