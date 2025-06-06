FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set up working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create data directory structure
RUN mkdir -p /app/data

# Copy application code
COPY . .

# Expose Ollama port
EXPOSE 11434

# Start Ollama and run the app (JSON format)
CMD ["bash", "-c", "ollama serve & sleep 5 && ollama pull $EMBEDDING_MODEL && ollama pull $LANGUAGE_MODEL && python app.py"]