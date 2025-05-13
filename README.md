# Multimodal Retrieval-Augmented Generation 

This project implements a Multimodal Retrieval-Augmented Generation (RAG) system capable of processing and querying information from PDF documents containing 
- text,
- images,
- tables, and
- formulas.

It integrates various components to extract, embed, index, and retrieve multimodal data, facilitating advanced question-answering capabilities.


 **<a href="https://unstructured.io/">Unstructured</a>**. 
 
1. [Leetcode Database Questions](#1)
   1. [Easy Questions](#2)  
   2. [Medium Questions](#3)
   3. [Hard Questions](#4) 
3. [Complete SQL Mastery](#5)  
 

<a name="1"></a>
## Leetcode Database Questions



    Multimodal-RAG-Application/
    ├── config.py                 # Configuration settings
    ├── embed/                    # Embedding generation modules
    │   └── clip_embedder.py      # CLIP-based embedding generator
    ├── extract/                  # PDF extraction modules
    │   ├── element_saver.py      # Saves extracted elements
    │   └── pdf_parser.py         # Parses PDF files
    ├── index/                    # Indexing modules
    │   └── faiss_index.py        # FAISS index creation
    ├── rag/                      # RAG model interaction
    │   └── rag_ollama.py         # Interfaces with LLaMA model
    ├── utils.py                  # Utility functions
    ├── main.py                   # Main execution script
    ├── requirements.txt          # Python dependencies
    └── README.md                 # Project documentation
