from embedder.embed import generate_embeddings

def test_generate_embeddings():
    text = "This is a test sentence."
    embeddings = generate_embeddings(text)
    assert isinstance(embeddings, list)
    assert len(embeddings) > 0
