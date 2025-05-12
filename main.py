# main.py

from config import BASE_DIR, DATA_DIR, OUTPUT_DIR
from utils import create_directories, download_pdf
from extract.element_saver import save_extracted_elements
from unstructured.partition.pdf import partition_pdf
from embed.clip_embedder import generate_multimodal_embeddings
from index.faiss_index import create_faiss_index
from rag.rag_ollama import invoke_llama
from extract.pdf_parser import extract_pdf_elements
import os
import numpy as np 
from IPython import display

# Add the correct poppler path to PATH
os.environ["PATH"] += os.pathsep + "/home/dan/anaconda3/pkgs/poppler-23.12.0-h590f24d_0/bin"

# Set the LD_LIBRARY_PATH for libtiff
libtiff_path = "/home/dan/anaconda3/envs/multimodal_rag/lib"
os.environ["LD_LIBRARY_PATH"] = libtiff_path + os.pathsep + os.environ.get("LD_LIBRARY_PATH", "")

# Add the conda environment binary path to PATH
os.environ["PATH"] += os.pathsep + "/home/dan/anaconda3/envs/multimodal_rag/bin"

def main():
    # Load the PDF and extract the elements
    # print (DATA_DIR)
    # print (BASE_DIR)
    create_directories(DATA_DIR)

    # Define the URL of the paper
    pdf_url = "https://arxiv.org/pdf/1706.03762.pdf"  # Attention is All You Need URL
    pdf_filename = "attention_paper.pdf"
    pdf_file_path = os.path.join(DATA_DIR, pdf_filename)

    # Check if the file already exists before downloading
    if not os.path.exists(pdf_file_path):
        download_pdf(pdf_url, pdf_file_path)

    pdf_elements = extract_pdf_elements(pdf_file_path)
    
    category_counts, items = save_extracted_elements(pdf_elements, DATA_DIR)
    print(category_counts)

    # Generate embeddings for each item
    for item in items:
        if item['type'] in ['text', 'table']:
            item['embedding'] = generate_multimodal_embeddings(prompt=item['text'])
        else:
            item['embedding'] = generate_multimodal_embeddings(image=item['image'])

    # Create FAISS index
    # all_embeddings = [item['embedding'] for item in items]

    # Determine the embedding dimension
    embedding_vector_dimension = len(items[0]['embedding'])

    all_embeddings = np.array([item['embedding'] for item in items], dtype=np.float32)


    embedding_vector_dimension = len(items[0]['embedding'])
    faiss_index = create_faiss_index(embedding_vector_dimension, all_embeddings)

    # Example: Query RAG model
    # query = "What is the main focus of the paper?"
    query = 'summarize the abstract'

    query_embedding = generate_multimodal_embeddings(prompt=query)#,output_embedding_length=embedding_vector_dimension)

    # Search for the nearest neighbors in the vector database
    distances, result = faiss_index.search(np.array(query_embedding, dtype=np.float32).reshape(1,-1), k=5)

    # Retrieve the matched items
    matched_items = [{k: v for k, v in items[index].items() if k != 'embedding'} for index in result.flatten()]


    response = invoke_llama(query, matched_items)  # Use first 5 items as example

    display.Markdown(response)

if __name__ == "__main__":
    main()
