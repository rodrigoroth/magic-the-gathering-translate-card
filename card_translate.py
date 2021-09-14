from preprocess_image import Preprocess
from fastapi import APIRouter
from schema import CardTranslate
from preprocess_text import preprocess_card

router = APIRouter()
preprocess = Preprocess()


@router.post('/card_translate64')
def translate_card(item: CardTranslate):
    text_translate = preprocess.image_tesseract(item.card)
    text_final = preprocess_card(text_translate)
    return {"card_name": text_final[0].replace('\n', " "), "card_type": text_final[1].replace('\n', " "), "card_text": text_final[2].replace('\n', " ")}
