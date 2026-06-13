import pdfplumber
from docx import Document

def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()

def extract_text_from_docx(file_path: str) -> str:
    document = Document(file_path)
    return "\n".join([paragraph.text for paragraph in document.paragraphs]).strip()

def extract_resume_text(file_path: str, filename: str) -> str:
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    if filename.endswith(".docx"):
        return extract_text_from_docx(file_path)

    raise ValueError("Only PDF and DOCX files are supported")