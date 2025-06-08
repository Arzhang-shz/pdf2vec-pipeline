# PDF Embedding Pipeline

This project provides a Python pipeline for processing PDF files, generating text embeddings, and saving them to either MongoDB or FAISS. It is designed to be modular and configurable, allowing you to easily switch between storage backends and customize the processing steps.

## Project Structure

The project has the following directory structure:

*   `pdf_processor/`: Contains the `extractor.py` file, which is responsible for extracting text from PDF files using the `PyMuPDF` library.
*   `embedder/`: Contains the `embed.py` file, which generates text embeddings using the `sentence-transformers` library.
*   `vector_stores/`: Contains the `faiss_handler.py` and `mongodb_handler.py` files, which handle saving embeddings to FAISS and MongoDB, respectively.
*   `pipelines/`: Contains the `run_pipeline.py` file, which orchestrates the PDF processing pipeline.
*   `scripts/`: Contains the `process_folder.py` script, which processes all PDF files in a given folder.
*   `tests/`: Contains the test suite for the project.

## Files

*   `pdf_processor/extractor.py`: Extracts text from PDF files using `PyMuPDF`. It also includes noise detection and removal using regular expressions.
*   `embedder/embed.py`: Generates text embeddings using the `sentence-transformers` library.
*   `vector_stores/faiss_handler.py`: Handles saving embeddings to a FAISS index.
*   `vector_stores/mongodb_handler.py`: Handles saving embeddings to a MongoDB database.
*   `pipelines/run_pipeline.py`: Orchestrates the PDF processing pipeline. It takes a PDF file as input, extracts text, generates embeddings, and saves them to either MongoDB or FAISS.
*   `scripts/process_folder.py`: Processes all PDF files in a given folder using the `run_pipeline.py` script.
*   `requirements.txt`: Contains the list of dependencies for the project.

## Configuration

The project can be configured using command-line arguments and environment variables.

### Command-Line Arguments

The `pipelines/run_pipeline.py` script accepts the following command-line arguments:

*   `pdf_path`: Path to the PDF file to process.
*   `--faiss_index_path`: Path to the FAISS index file. Defaults to `faiss_index.faiss`.
*   `--chunk_size`: Chunk size for text splitting. Defaults to 512.

### Environment Variables

The `vector_stores/mongodb_handler.py` file uses the following environment variables to configure the MongoDB connection:

*   `MONGODB_URI`: MongoDB connection URI. Defaults to `mongodb://localhost:27017/`.
*   `MONGODB_DB`: MongoDB database name. Defaults to `pdf_embeddings`.
*   `MONGODB_COLLECTION`: MongoDB collection name. Defaults to `embeddings`.

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd pdf2vec-pipeline
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Process a single PDF file:**

    ```bash
    PYTHONPATH=. python pipelines/run_pipeline.py <pdf_file_path> --faiss_index_path <faiss_index_path> --chunk_size <chunk_size>
    ```

2.  **Process all PDFs in a folder:**

    ```bash
    python scripts/process_folder.py <folder_path>
    ```

## Example

To process a single PDF file:

```bash
PYTHONPATH=. python pipelines/run_pipeline.py data/example.pdf --faiss_index_path faiss_index.faiss --chunk_size 512
```

**Note:** Replace `<pdf_file_path>`, `<folder_path>`, `<faiss_index_path>`, and `<chunk_size>` with the actual paths and values.
