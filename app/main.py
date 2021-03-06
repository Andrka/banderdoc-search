# -*- coding:utf-8 -*-

from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Query

from app.schemas import TextPiece, TextType

TEST_TEXT_PIECES = (
    TextPiece(**{
        'text': 'text1',
        'type': 'paragraph',
        'page_number': 1,
        'document_name': 'doc1',
    }),
    TextPiece(**{
        'text': 'text2',
        'type': 'paragraph',
        'page_number': 2,
        'document_name': 'doc2',
    }),
    TextPiece(**{
        'text': 'text3',
        'type': 'title',
        'page_number': 3,
        'document_name': 'doc3',
    }),
)

app = FastAPI()


@app.post('/text-pieces/')
def index_text_piece(text_piece: TextPiece):
    return text_piece


@app.get('/text-pieces/', response_model=List[TextPiece])
def get_text_pieces(
    text: Optional[str] = Query(None),
    type: Optional[TextType] = Query(None),
    page_number: Optional[int] = Query(None, gt=0),
    document_name: Optional[str] = Query(None),
):
    result = TEST_TEXT_PIECES
    if text:
        result = [x for x in result if x.text == text]
    if type:
        result = [x for x in result if x.type == type]
    if page_number and document_name:
        result = [x for x in result if ((
            x.page_number == page_number
        ) and (
            x.document_name == document_name
        ))]
    return result


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=80, reload=True)
