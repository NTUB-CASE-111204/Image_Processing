# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#img_name = 'C:/chashin/2技/python文字辨識/demo-en-us.png'
#img_name = 'C:/chashin/2技/python文字辨識/002-zh-cht.png'
#img_name = 'C:/chashin/2技/python文字辨識/goro4.png'
#img_name = 'C:/chashin/2技/python文字辨識/goro2.jpg'
#img_name = 'C:/chashin/2技/python文字辨識/PATTIS.png'
#img_name = 'C:/chashin/2技/python文字辨識/IRITA.png'
#img_name = 'C:/chashin/2技/python文字辨識/chih.jpg'
img_name = 'C:/chashin/2技/python文字辨識/ONE.jpg'
img = Image.open(img_name)
text = pytesseract.image_to_string(img, lang='eng+chi_tra')
print(text)
#print("text")