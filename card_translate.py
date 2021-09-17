from preprocess_image import Preprocess
from fastapi import APIRouter
from schema import CardTranslate
from preprocess_text import preprocess_card
from web_search import scrape_google

router = APIRouter()
preprocess = Preprocess()


@router.post('/card_translate64')
def translate_card(item: CardTranslate):
    text_translate = preprocess.image_tesseract(item.card)
    text_final = preprocess_card(text_translate)
    print(scrape_google("uril the mistalker"))
    return {"card_name": text_final[0], "card_type": text_final[1], "card_text": text_final[2]}
