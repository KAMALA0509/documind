"""
Uses `pypdf` because it is lightweight and sufficient for text-based PDFs.
OCR support is intentionally excluded from the current implementation.
"""
import io
import logging

from pypdf import PdfReader

logger = logging.getLogger("documind")


class PDFExtractionError(Exception):
    """Raised when a PDF can't be read or contains no extractable text."""


def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        reader = PdfReader(io.BytesIO(file_bytes))
    except Exception as exc:
        raise PDFExtractionError(f"Could not open PDF: {exc}") from exc

    if reader.is_encrypted:
        raise PDFExtractionError("PDF is password-protected; cannot extract text")

    pages_text = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if text.strip():
            pages_text.append(text)
        else:
            logger.warning("Page %d had no extractable text (likely scanned image)", page_num)

    full_text = "\n\n".join(pages_text)

    if not full_text.strip():
        raise PDFExtractionError(
            "No extractable text found — this PDF may be a scanned image "
            "without an OCR text layer"
        )

    return full_text
