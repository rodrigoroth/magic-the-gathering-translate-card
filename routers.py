from fastapi import APIRouter
import card_translate


api_router = APIRouter()


api_router.include_router(card_translate.router)