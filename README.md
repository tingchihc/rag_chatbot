# rag_chatbot


```
docker build -t ollama-rag .
docker run -p 11434:11434 --env EMBEDDING_MODEL="hf.co/CompendiumLabs/bge-base-en-v1.5-gguf" --env LANGUAGE_MODEL="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF" -it ollama-rag
```
