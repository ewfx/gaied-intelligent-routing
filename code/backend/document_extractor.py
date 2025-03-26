from PyPDF2 import PdfReader
from docx import Document

class DocumentExtractor:
    @staticmethod
    def extract_text(file_path: str, file_type: str) -> str:
        if file_type == "pdf":
            with open(file_path, "rb") as f:
                pdf = PdfReader(f)
                text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            return text

        elif file_type == "docx":
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text

        elif file_type == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            return text
