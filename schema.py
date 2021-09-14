from pydantic import BaseModel


class CardTranslate(BaseModel):
    card: str
