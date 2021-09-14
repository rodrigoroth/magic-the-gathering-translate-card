import pytesseract
import base64
from PIL import Image
import io
import cv2
import numpy as np


class Preprocess:

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    def process64(self, filepath):
        base64_img = filepath.encode('utf-8')
        base64_bytes = base64.b64decode(base64_img)
        bytes_obj = io.BytesIO(base64_bytes)
        image = Image.open(bytes_obj)

        return image

    def preprocess_image(self, image):
        image_pre = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        image_pre = cv2.resize(image_pre, (380, 580), interpolation=cv2.INTER_CUBIC)

        # cv2.imshow('test', image_pre)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        image_pre = cv2.cvtColor(image_pre, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        image_pre = cv2.dilate(image_pre, kernel, iterations=1)
        image_pre = cv2.erode(image_pre, kernel, iterations=1)
        image_pre = cv2.adaptiveThreshold(cv2.bilateralFilter(image_pre, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        filtered = cv2.adaptiveThreshold(image_pre.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
        opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        or_image = cv2.bitwise_or(image_pre, closing)
        card_name = or_image[10:90, 0:350]
        card_type = image_pre[330:360, 0:360]
        card_text = or_image[350:540, 0:360]
        # cv2.imshow('test', card_name)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return [card_name, card_type, card_text]

    def image_tesseract(self, image):
        image_pre = self.process64(image)
        card_list = self.preprocess_image(image_pre)
        cards_list = []
        for card in card_list:
            cards = pytesseract.image_to_string(card, lang='eng')
            cards_list.append(cards)

        return cards_list

