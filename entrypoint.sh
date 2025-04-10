#!/bin/bash
set -e

# Start Ollama in the background
ollama serve &

# Wait for Ollama to start up
echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434/api/tags >/dev/null 2>&1; do
    sleep 1
done

# Pull the required models
echo "Pulling embedding model..."
ollama pull $EMBEDDING_MODEL
echo "Pulling language model..."
ollama pull $LANGUAGE_MODEL

# Run the application
echo "Starting application..."
python app.py