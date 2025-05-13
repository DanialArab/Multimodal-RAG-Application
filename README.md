# Multimodal Retrieval-Augmented Generation 

In this project, I implemented a Multimodal Retrieval-Augmented Generation (RAG) system capable of processing and querying information from PDF documents containing 
- text,
- images,
- tables, and
- formulas.

It integrates various components to extract, embed, index, and retrieve multimodal data, facilitating advanced question-answering capabilities.

1. [Intro](#1)
2. [Tech stack](#2)
3. [Repository structures](#3)
4. [Pipeline](#4)
   1. [Getting the Document](#5)
   2. [Document Element Extraction](#6)
   3. [Multimodal Embedding Generation](#7)
   4. [Vector Indexing](#8)
   5. [Retrieval & Answer Generation](#9)
5. [Results and discussion ](#10)
   1. [query_1 = "How is the marginal likelihood is calculated?"](#11)
   2. [query_2 = "What does reparameterization of the variational lower bound yield?](#12)
   3. [query_3 = "What algorithm was proposed?"](#13)
   4. [query_4 = query = "What is the trick that was discussed?"](#14)
   5. [query_5 = "How are Parameters updated?"](#15)




<a name="1"></a>
## Intro
Traditional question-answering systems often rely solely on text data, which limits their effectiveness when dealing with complex, information-dense documents like PDFs that contain images, tables, formulas, etc. This project extends the Retrieval-Augmented Generation paradigm by handling multimodal inputs.

The key idea is to :
- parse different elements (text, images, tables, formulas) from a PDF.
- -convert them into a unified embedding space using CLIP.
- index those embeddings using FAISS.
- retrieve and generate answers to natural language queries using a language model (LLamA) enhanced by relevant context.

<a name="2"></a>
## Tech stack

The following technologies were used to build this project:

- Data handling: **<a href="https://unstructured.io/">Unstructured</a>** is used for all kind of data extraction and parsing
- Embedding: The Contrastive Language-Image Pretraining (CLIP) model is used to generate embeddings. It jointly embeds images and text into the same vector space, enabling comparison between the two.
- Vector Search: FAISS is used for similarity search and building a searchable index of embeddings to perform fast and scalable similarity queries.
- LLM Deployment: Ollama is used for lightweight and efficient hosting and deployment of large language models (LLMs).

<a name="3"></a>
## Repository structure

Here is the project structure with a brief description on the functionality of each module:

    Multimodal-RAG-Application/
    ├── config.py                 # Configuration settings
    ├── embed/                    # Embedding generation modules
    │   └── clip_embedder.py      # CLIP-based embedding generator
    ├── extract/                  # PDF extraction modules
    │   ├── element_saver.py      # Saves extracted elements
    │   └── pdf_parser.py         # Parses PDF files using unstructured library 
    ├── index/                    # Indexing modules
    │   └── faiss_index.py        # FAISS index creation
    ├── rag/                      # RAG model interaction
    │   └── rag_ollama.py         # Interfaces with Llama model
    ├── utils.py                  # Utility functions
    ├── main.py                   # Main execution script
    ├── requirements.txt          # Python dependencies
    └── README.md                 # Project documentation


<a name="4"></a>
## Pipeline

<a name="5"></a>
### Getting the Document
A PDF file for which the link is provided (e.g., as an example “Auto-Encoding Variational Bayes” article was chosen for proof of concept) is downloaded and stored  in a specified DATA_DIR.

<a name="6"></a>
### Document Element Extraction
Uses the unstructured library to parse the PDF into elements:

- Text blocks (narrative, header, footer)
- Images
- Tables
- Formulas

Saves each element as a separate file or entry for later processing.

<a name="7"></a>
### Multimodal Embedding Generation 
Uses CLIP to generate embeddings for:
- Raw images
- Visual representations of tables/formulas
- Plain text blocks

Embeddings are normalized and stored in a list.

<a name="8"></a>
### Vector Indexing
All embeddings are indexed using FAISS (IndexFlatL2) to enable fast vector similarity search.

<a name="9"></a>
### Retrieval & Answer Generation
Here are the steps to retrieve the answer:
- First, the embedding for the query needs to be generated,
- then the top-k most similar elements using the FAISS index will be retrieved
- the retrieved context is fed into Llama model via Ollama 

<a name="10"></a>
## Results and discussion 

Here are some queries and the RAG response as a POC:

<a name="11"></a>
## query_1 = "How is the marginal likelihood is calculated?"

RAG response:

      The marginal likelihood is calculated as a sum over the marginal likelihoods of individual datapoints, which can be expressed as:
      
      log p(x₁, ..., xₙ) = ∑[log p(xᵢ)]
      
      where p(xᵢ) is the marginal likelihood of each individual datapoint xᵢ.
      
      This can be further rewritten using equations (20) and (18) to derive a Monte Carlo estimate of the variational lower bound for a given datapoint x(i), which involves choosing a prior p(θ) and a function g(θ, x) that satisfies certain conditions.
      
      In essence, the marginal likelihood calculation involves summing up the logarithmic probabilities of each individual datapoint in the dataset.

<a name="12"></a>
## query_2 = "What does reparameterization of the variational lower bound yield?"

RAG response:

      The reparameterization of the variational lower bound yields a Stochastic Gradient Variational Bayes (SGVB) estimator, denoted as ~ L(0, ; x). This allows for the application of stochastic gradient descent to optimize the variational parameters, making it possible to learn the model using backpropagation. The reparameterization trick enables the Monte Carlo estimation of the variational lower bound, which is a key component of Variational Autoencoders (VAEs) and other deep generative models.

      In essence, reparameterization helps to:
      
      Convert a non-differentiable stochastic node into a differentiable one.
      Enable backpropagation through the variational lower bound, allowing for end-to-end learning of the model.
      Improve the stability and efficiency of training by avoiding the need for REINFORCE-style score function estimators.
      By reparameterizing the variational lower bound, you can obtain a more efficient and stable estimate of the evidence lower bound (ELBO), which is essential for training VAEs and other deep generative models.

<a name="13"></a>
## query_3 = "What algorithm was proposed?"

RAG response:

      The algorithm is the Auto-Encoding Variational Bayes (AEVB) algorithm, which uses the Stochastic Gradient Variational Bayes (SGVB) estimator to optimize a recognition model for efficient approximate posterior inference.

<a name="14"></a>
## query_4 = "What is the trick that was discussed?"

RAG response:

      The trick that was discussed is called the "reparameterization trick". This trick allows for the differentiation of the variational lower bound with respect to the variational parameters, which is necessary for optimizing the model. The reparameterization trick involves expressing the latent variables as a deterministic function of the variational parameters and a random noise variable, which enables backpropagation through the latent space.



<a name="15"></a>
## query_5 = "How are Parameters updated?"

RAG response:

      The parameters are updated using stochastic gradient methods, specifically the Adagrad algorithm with a global stepsize parameter chosen from {0.01, 0.02, 0.1} based on performance on the training set in the first few iterations. The parameters, both variational and generative, are initialized by random sampling from N(0,0.01) and are jointly stochastically optimized using the MAP criterion. Minibatches of size M = 100 are used, with L = 1 samples per datapoint.

      To be more specific, the parameter updates are done as follows:

      The variational lower bound is reparameterized to obtain a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods.
      The Adagrad algorithm is used to adapt the stepsizes for the parameter updates.
      The global stepsize parameters are chosen from {0.01, 0.02, 0.1} based on performance on the training set in the first few iterations.
      Minibatches of size M = 100 are used, with L = 1 samples per datapoint.
      This process allows for efficient inference and learning in directed probabilistic models with continuous latent variables and large datasets.
