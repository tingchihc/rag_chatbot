# rag_chatbot

This repository contains a RAG system implemented using Ollama. The code allows you to query a local dataset of car-related information using natural language questions, with responses generated by a language model based on relevant retrieved content.

## Features  
- Local vector database storing document chunks
- Semantic search using embeddings from the bge-base-en-v1.5 model
- Text generation using Llama-3.2-1B-Instruct
- Simple cosine similarity implementation for retrieval
- Interactive command-line interface

## How It Works

- The system loads text data from three files in the ```data``` directory
- Each text chunk is embedded and stored in an in-memory vector database
- When you ask a question, it:
  - Embeds your query
  - Finds the most relevant document chunks using cosine similarity
  - Feeds those chunks as context to the language model
  - Returns a response based only on the provided context

## Run

```
docker build -t ollama-rag .
```
```
docker run -p 11434:11434 --env EMBEDDING_MODEL="hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"  
                          --env LANGUAGE_MODEL="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"
                          -it ollama-rag
```

## Notice
- <b>Limited Dataset</b>: The current implementation uses a very small dataset (just three text files). For production use or more accurate results, you should expand the dataset significantly. The retrieval quality is directly tied to the comprehensiveness of your data.
- <b>Basic Retrieval Method</b>: The retrieval mechanism uses simple cosine similarity which may not always return the most contextually relevant results. More sophisticated retrieval methods (like reranking or hybrid search) could improve response quality.
- <b>Model Flexibility</b>: The current language model (Llama-3.2-1B-Instruct) may have limited reasoning capabilities for complex RAG applications. You can easily swap it for a more powerful model in the ```LANGUAGE_MODEL``` variable to improve response quality and reasoning abilities.
- <b>Experimental Status</b>: This implementation is intended as a demonstration rather than a production-ready system. Consider this a starting point for building more robust RAG applications.

# Acknowledge  
- https://huggingface.co/blog/ngxson/make-your-own-rag  

