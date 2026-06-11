from PyPDF2 import PdfReader
def extract_pdf(pdf_path):
    """Extract text from uploaded PDF file."""
    reader = PdfReader(pdf_path)
    text=""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text