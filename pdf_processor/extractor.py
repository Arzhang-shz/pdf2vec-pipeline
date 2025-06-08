import fitz
import re

def extract_text_from_pdf(path: str) -> str:
    """
    Opens a PDF file.
    Extracts and returns clean text.
    Uses PyMuPDF (fitz).
    """
    text = ""
    try:
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()

        # Remove noise
        text = remove_noise(text)
    except Exception as e:
        print(f"Error extracting text from {path}: {e}")
    return text

def remove_noise(text: str) -> str:
    """
    Removes noise from the extracted text.
    """
    # Define noise patterns
    noise_patterns = [
        r"Page \d+",  # Page numbers
        r"^\s*$",  # Empty lines
    ]

    for pattern in noise_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)
    return text
