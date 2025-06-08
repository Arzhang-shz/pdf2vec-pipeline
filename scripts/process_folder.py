import os
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Process all PDFs in a folder using run_pipeline.py")
    parser.add_argument("folder_path", help="Path to the folder containing PDF files")
    args = parser.parse_args()

    folder_path = args.folder_path
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"Processing: {pdf_path}")
            try:
                subprocess.run(["python", os.path.join(os.path.dirname(__file__), "../pipelines/run_pipeline.py"), pdf_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error processing {pdf_path}: {e}")

if __name__ == "__main__":
    main()
