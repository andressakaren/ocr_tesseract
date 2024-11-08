import cv2
import pytesseract
import pyttsx3
# C:\Program Files\Tesseract-OCR

img = cv2.imread('img1.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\Tesseract.exe'
resultado = pytesseract.image_to_string(img)
engine = pyttsx3.init()
print(resultado)
engine.say(resultado)
engine.runAndWait()


