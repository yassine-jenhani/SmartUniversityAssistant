from pathlib import Path
import pymupdf
from docx import Document


SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def extract_pdf(file_path: str) -> list:
    """Extract text page by page from a PDF."""
    pages = []

    with pymupdf.open(file_path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()

            if text:
                pages.append({
                    "page_number": page_number,
                    "text": text
                })

    return pages


def extract_docx(file_path: str) -> list:
    """Extract paragraphs from a Word document."""
    document = Document(file_path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    )

    return [{
        "page_number": None,
        "text": text
    }] if text else []


def extract_txt(file_path: str) -> list:
    """Extract text from a TXT file."""
    text = Path(file_path).read_text(encoding="utf-8-sig").strip()

    return [{
        "page_number": None,
        "text": text
    }] if text else []


def extract_document(file_path: str) -> dict:
    """Detect the file format and extract its content."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file format: {extension}")

    if extension == ".pdf":
        pages = extract_pdf(str(path))

    elif extension == ".docx":
        pages = extract_docx(str(path))

    else:
        pages = extract_txt(str(path))

    return {
        "filename": path.name,
        "file_type": extension,
        "total_pages": len(pages) if extension == ".pdf" else None,
        "pages": pages
    }
