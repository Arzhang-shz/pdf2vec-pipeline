from pymongo import MongoClient

def save_to_mongodb(embedding: list[float], metadata: dict):
    """
    Connects to a MongoDB collection.
    Inserts the embedding and metadata into the DB.
    """
    import os
    try:
        mongo_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
        db_name = os.environ.get('MONGODB_DB', 'pdf_embeddings')
        collection_name = os.environ.get('MONGODB_COLLECTION', 'embeddings')
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]

        document = {
            'embedding': embedding,
            'metadata': metadata
        }
        collection.insert_one(document)
        client.close()
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")
