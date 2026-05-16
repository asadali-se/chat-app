from pydantic import BaseModel
from datetime import datetime


class ConversationBase(BaseModel):
    user1_id: int
    user2_id: int


class ConversationCreate(ConversationBase):
    pass


class ConversationResponse(ConversationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
