# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img_name = 'C:/chashin/2技/python文字辨識/demo-en-us.png'
img = Image.open(img_name)
text = pytesseract.image_to_string(img, lang='eng')
print(text)
print("text")