import faiss
import numpy as np
import os

def save_to_faiss(embedding: list[float], metadata: dict, index_path: str):
    """
    Loads or creates a FAISS index (cosine similarity).
    Adds the embedding to the index and saves it to disk.
    """
    embedding_array = np.array([embedding]).astype('float32')
    index = None
    if os.path.exists(index_path):
        index = faiss.read_index(index_path)
    else:
        dimension = len(embedding)
        index = faiss.IndexFlatIP(dimension)  # IndexFlatIP for inner product (cosine similarity)

    index.add(embedding_array)
    faiss.write_index(index, index_path)
