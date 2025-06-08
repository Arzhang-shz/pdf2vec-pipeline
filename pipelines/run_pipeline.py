import argparse
import logging
import os
from pdf_processor.extractor import extract_text_from_pdf
from embedder.embed import generate_embeddings
from vector_stores.mongodb_handler import save_to_mongodb
from vector_stores.faiss_handler import save_to_faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(
        description="Process PDF, generate embeddings, and save to MongoDB and/or FAISS."
    )
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument(
        "--faiss_index_path", default="faiss_index.faiss", help="Path to the FAISS index file"
    )
    parser.add_argument("--chunk_size", type=int, default=512, help="Chunk size for text splitting")
    parser.add_argument(
        "--store",
        choices=["mongo", "faiss", "both"],
        default=os.getenv("EMBEDDING_STORE", "both"),
        help="Where to store embeddings: mongo, faiss, or both"
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="If set, only prints summary info (for debugging or reporting)"
    )

    args = parser.parse_args()
    pdf_path = args.pdf_path

    try:
        text = extract_text_from_pdf(pdf_path)
    except Exception as e:
        logging.error(f"Error extracting text from {pdf_path}: {e}")
        return

    if args.summary:
        logging.info(f"Summary mode: processed {pdf_path}")
        return

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=args.chunk_size,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = text_splitter.split_text(text)

    for chunk in chunks:
        try:
            embedding = generate_embeddings(chunk)
            metadata = {"pdf_path": pdf_path}

            if args.store in ["mongo", "both"]:
                save_to_mongodb(embedding, metadata)

            if args.store in ["faiss", "both"]:
                save_to_faiss(embedding, metadata, args.faiss_index_path)

        except Exception as e:
            logging.error(f"Error processing chunk from {pdf_path}: {e}")

if __name__ == "__main__":
    main()
