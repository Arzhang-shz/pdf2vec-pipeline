import pytest
from ..pdf_processor.extractor import extract_text_from_pdf
from reportlab.pdfgen import canvas
import os

def test_extract_text_from_pdf():
    # Create a dummy PDF file for testing
    c = canvas.Canvas("test.pdf")
    c.drawString(100, 750, "This is a test PDF file.")
    c.save()

    text = extract_text_from_pdf("test.pdf")
    assert "This is a test PDF file." in text

    # Clean up the dummy file
    os.remove("test.pdf")
