import numpy as np
import faiss

def create_faiss_index(embedding_vector_dimension, all_embeddings):
    index = faiss.IndexFlatL2(embedding_vector_dimension)
    index.reset()
    index.add(all_embeddings)
    return index



