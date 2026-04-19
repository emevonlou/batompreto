import mss
import pytesseract
from PIL import Image, ImageFilter, ImageOps


def preprocess_for_ocr(img: Image.Image) -> Image.Image:
    img = ImageOps.grayscale(img)
    img = img.point(lambda p: 255 if p > 150 else 0)
    img = img.resize((img.width * 2, img.height * 2))
    img = img.filter(ImageFilter.SHARPEN)
    return img


def capture_chat(region: dict, lang: str) -> str:
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        img = preprocess_for_ocr(img)
        config = "--psm 6 -c preserve_interword_spaces=1"
        text = pytesseract.image_to_string(img, lang=lang, config=config)
        return text.strip()
