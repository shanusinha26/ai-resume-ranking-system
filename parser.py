import pdfplumber
import docx
import re

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_email(text):
    emails = re.findall(r'\S+@\S+', text)
    return emails[0] if emails else "Not Found"


def extract_phone(text):
    import re
    
    phone_pattern = r'(\+?\d[\d\s\-]{8,15}\d)'
    phones = re.findall(phone_pattern, text)
    
    return phones[0] if phones else "Not Found"