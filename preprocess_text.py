import re
from textblob import TextBlob
from textblob.en import Spelling

pathToFile = "/home/rodrigo/Downloads/train_magic.txt"
spelling = Spelling(path=pathToFile)


def preprocess_card(list_cards):
    card_name = list_cards[0].replace('\n', "").replace('\f', "")
    card_name = re.sub("[^a-zA-Z]+", ' ', card_name)
    card_type = list_cards[1].replace('\n', "").replace('\f', "")
    card_type = re.sub("[^a-zA-Z]+", ' ', card_type)
    card_text = list_cards[2].replace('\n', " ").replace('\f', " ")
    # card_text = TextBlob(card_text).correct()
    corrected = " "
    for i in card_text:
        corrected = corrected + spelling.suggest(i)[0][0]
    print(corrected)

    if card_type[0].islower():
        card_type = card_type.replace(card_type[0], "")
    if card_name[0].islower():
        card_name = card_name.replace(card_name[0], "")

    return [card_name, card_type, card_text]
