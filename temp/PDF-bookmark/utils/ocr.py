import pytesseract

def extract_text(image_file, lang='chi_sim'):
    # Use OCR to extract text from an image file
    text = pytesseract.image_to_string(image_file, lang=lang, config = '--psm 6 --oem 1')
    return text
