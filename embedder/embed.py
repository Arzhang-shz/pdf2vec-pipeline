from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text: str) -> list[float]:
    """
    Uses sentence-transformers (e.g., all-MiniLM-L6-v2) to generate and return an embedding.
    """
    embeddings = model.encode(text)
    return embeddings.tolist()
