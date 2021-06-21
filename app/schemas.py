# -*- coding:utf-8 -*-

from enum import Enum

from pydantic import BaseModel


class TextType(str, Enum):
    paragraph = 'paragraph'
    title = 'title'


class TextPiece(BaseModel):
    text: str
    type: TextType
    page_number: int
    document_name: str
