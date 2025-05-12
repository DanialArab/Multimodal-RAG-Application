import numpy as np
import faiss

def create_faiss_index(embedding_vector_dimension, all_embeddings):
    # embedding_dim = len(items[0]['embedding'])
    # # all_embeddings = np.array([item['embedding'] for item in items], dtype=np.float32)
    index = faiss.IndexFlatL2(embedding_vector_dimension)
    index.reset()
    index.add(all_embeddings)
    return index



