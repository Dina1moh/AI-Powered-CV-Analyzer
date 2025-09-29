#text_extractor.py 
from pypdf import PdfReader 

def get_pdf_text(pdf_doc):
    text=""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text +=page.extract_text()
    return text

     