from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from docx import Document


def extract_text(file_path: Path) -> str:
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return extract_pdf_text(file_path)

    if suffix == ".docx":
        return extract_docx_text(file_path)

    raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")


def extract_pdf_text(file_path: Path) -> str:
    loader = PyMuPDFLoader(str(file_path))
    docs = loader.load()

    return "\n\n".join(doc.page_content for doc in docs)


def extract_docx_text(file_path: Path) -> str:
    document = Document(str(file_path))

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n\n".join(paragraphs)