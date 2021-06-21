# -*- coding:utf-8 -*-

import uvicorn
from fastapi import FastAPI

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
    return text_piece.json()


@app.get('/text-pieces/')
def get_text_pieces(
    text: str = None,
    type: TextType = None,
    page_number: int = None,
    document_name: str = None,
):
    result = list(TEST_TEXT_PIECES)
    if text:
        result = filter(lambda x: x.text == text, result)
    if type:
        result = filter(lambda x: x.type == type, result)
    if page_number and document_name:
        result = filter(
            (lambda x: x.page_number == page_number
                and x.document_name == document_name),
            result,
            )
    return list(map(lambda x: x.json(), result))


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=80, reload=True)
