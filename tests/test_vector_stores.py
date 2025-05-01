import pytest
from ..vector_stores.mongodb_handler import save_to_mongodb
from ..vector_stores.faiss_handler import save_to_faiss
import os
import faiss
import pymongo

def test_mongodb_insertion():
    embedding = [0.1, 0.2, 0.3]
    metadata = {"test": "test"}
    try:
        save_to_mongodb(embedding, metadata)
        # Add assertion to check if the data was actually inserted
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['pdf_embeddings']
        collection = db['embeddings']
        assert collection.count_documents({"metadata.test": "test"}) > 0
        collection.delete_many({"metadata.test": "test"}) # Clean up
        client.close()
    except Exception as e:
        pytest.fail(f"MongoDB insertion failed: {e}")

def test_faiss_index_creation_and_retrieval():
    embedding = [0.1, 0.2, 0.3]
    metadata = {"test": "test"}
    index_path = "test_index.faiss"
    try:
        save_to_faiss(embedding, metadata, index_path)
        assert os.path.exists(index_path)
        index = faiss.read_index(index_path)
        assert index.ntotal == 1
    except Exception as e:
        pytest.fail(f"FAISS index creation/retrieval failed: {e}")
    finally:
        if os.path.exists(index_path):
            os.remove(index_path)
