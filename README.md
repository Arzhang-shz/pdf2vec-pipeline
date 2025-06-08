# PDF Embedding Pipeline

This project provides a Python pipeline for processing PDF files, generating text embeddings, and saving them to either MongoDB or FAISS.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd pdf-embedding-pipeline
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1.  **Process a single PDF file:**

    ```bash
    python pipelines/run_pipeline.py <pdf_file_path>
    ```

2.  **Process all PDFs in a folder:**

    ```bash
    python scripts/process_folder.py <folder_path>
    ```

## Example

To process a single PDF file:

```bash
python pipelines/run_pipeline.py data/example.pdf
```

**Note:** Replace `<pdf_file_path>` and `<folder_path>` with the actual paths to the PDF file or folder.
