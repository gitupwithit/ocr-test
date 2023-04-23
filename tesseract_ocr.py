import sys
import pytesseract
from PIL import Image

def ocr_image(image_path):
    pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
    text = pytesseract.image_to_string(Image.open(image_path))
    return text.strip()

if __name__ == "__main__":
    image_path = sys.argv[1]
    result = ocr_image(image_path)
    print(result)
