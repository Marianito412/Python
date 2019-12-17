import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('Breaking_News.png')
text = pytesseract.image_to_string(img)
print(text)
