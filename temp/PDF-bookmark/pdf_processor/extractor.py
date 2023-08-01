from utils import ocr
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
import shutil, os
from PIL import Image, ImageFilter, ImageOps
import os

def gray_image(image, output_path):
    # Convert the image to grayscale
    gray = ImageOps.grayscale(image)
    # Apply a median filter to remove noise
    gray = gray.filter(ImageFilter.MedianFilter(size=3))

    gray.save(output_path)

    return gray

def preprocess_image(gray_image, output_path):
    # Threshold the image to create a binary image
    threshold = 210
    preprocessed_image = gray_image.point(lambda x: 0 if x < threshold else 255)
    
    # Save the preprocessed image
    preprocessed_image.save(output_path)
    
    return preprocessed_image

def extract_toc(pdf_file, start_page, end_page, lang='chi_sim'):
    # Determine if the PDF is a photocopy or pure text
    if is_photocopy(pdf_file):
        # Use OCR to extract the table of contents
        temp_dir = 'C:\\my_temp_dir'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        images = convert_from_path(pdf_file, output_folder=temp_dir, first_page=start_page, last_page=end_page, poppler_path=r"S:\\poppler-23.07.0\\Library\\bin")
        toc = ""
        for i, image in enumerate(images):
            # Preprocess the image and save it to temp_dir
            gray_image_path = os.path.join(temp_dir, f'grayed_{i}.png')
            preprocessed_image_path = os.path.join(temp_dir, f'preprocessed_{i}.png')
            grayed_image = gray_image(image, gray_image_path)
            preprocessed_image = preprocess_image(grayed_image, preprocessed_image_path)
            
            # Extract text from the preprocessed image
            toc += ocr.extract_text(image, lang=lang)
        # shutil.rmtree(temp_dir)
    else:
        # Extract the text directly from the PDF file
        toc = ""
        with open(pdf_file, 'rb') as f:
            reader = PdfFileReader(f)
            for page in range(start_page - 1, end_page - 1):
                toc += reader.getPage(page).extractText()
    return toc

def is_photocopy(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        page_text = ""
        for page in range(3, pdf_reader.numPages, 10):
            page_obj = pdf_reader.getPage(page)
            page_text += page_obj.extractText()
        if not page_text.strip():
            return True
    return False

