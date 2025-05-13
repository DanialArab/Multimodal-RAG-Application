# Multimodal_RAG

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
