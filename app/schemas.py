# -*- coding:utf-8 -*-

from enum import Enum

from pydantic import BaseModel, Field


class TextType(str, Enum):
    paragraph = 'paragraph'
    title = 'title'


class TextPiece(BaseModel):
    text: str
    type: TextType
    page_number: int = Field(gt=0)
    document_name: str
