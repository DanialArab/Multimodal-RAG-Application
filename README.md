# Multimodal_RAG


This project implements a Multimodal Retrieval-Augmented Generation (RAG) system capable of processing and querying information from PDF documents containing 
- text,
- images,
- tables, and
- formulas.

It integrates various components to extract, embed, index, and retrieve multimodal data, facilitating advanced question-answering capabilities.


my solutions to **Leetcode - Database questions using SQL**. The Leetcode databases are first needed to be regenerated in my MySQL server using the SQL Schema, presented along with each Leetcode question. This is required to be able to make a query in the Jupyter Notebook. All of my solutions are presented using Pandas API in Jupyter Notebook **<a href="https://github.com/DanialArab/SQL/blob/master/Leetcode%20Database%20Questions/Leetcode_Database_Questions_Pandas_API.ipynb">Leetcode Database Questions - Pandas API</a>**. Also, I leveraged Spark SQL API to re-solve the Leetcode - Database questions, which are detailed in the Jupyter Notebook file **<a href="https://github.com/DanialArab/SQL/blob/master/Leetcode%20Database%20Questions/Leetcode_Database_Questions_Spark_SQL_API.ipynb">Leetcode Database Questions - Spark SQL API</a>**. This repo contains the following directories and each one contains the pertinent files including README and Jupyter Notebook files: 
 
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
