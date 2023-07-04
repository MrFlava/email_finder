import re
from os import path, getpid, remove

import cv2
import pytesseract
from PIL import Image


preprocess = "thresh"

basedir = path.abspath(path.dirname(__file__))

image_path = path.join(basedir, "image/example.png")

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

filename = f"{getpid()}.png"
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
remove(filename)
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)


cv2.imshow("Image", image)
cv2.imshow("Output", gray)
