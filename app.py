import ollama
import os

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

def load_dataset():
    dataset = []
    #current_file = os.path.abspath(__file__)
    #project_root = os.path.dirname(os.path.dirname(current_file))

    DATA_F1 = os.path.join("data", "car1.txt")
    DATA_F2 = os.path.join("data", "car2.txt")
    DATA_F3 = os.path.join("data", "car3.txt")

    with open(DATA_F1, 'r') as file:
        dataset.extend(file.readlines())
    
    with open(DATA_F2, 'r') as file:
        dataset.extend(file.readlines())
    
    with open(DATA_F3, 'r') as file:
        dataset.extend(file.readlines())

    return dataset

def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
    VECTOR_DB.append((chunk, embedding))

def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])
    norm_a = sum([x ** 2 for x in a]) ** 0.5
    norm_b = sum([x ** 2 for x in b]) ** 0.5
    return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((chunk, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]


data = load_dataset()
VECTOR_DB = []

for i, chunk in enumerate(data):
    add_chunk_to_database(chunk)
    print(f'Added chunk {i+1}/{len(data)} to the database')

while True:
    input_query = input("\nAsk your question (or type 'exit' to quit): ")

    if input_query.strip().lower() == 'exit':
        print("Goodbye!")
        break
    
    retrieved_knowledge = retrieve(input_query)

    joined_chunks = '\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])
    instruction_prompt = f'''You are a helpful chatbot.
    Use only the following pieces of context to answer the question. Don't make up any new information:
    {joined_chunks}
    '''

    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {'role': 'system', 'content': instruction_prompt},
            {'role': 'user', 'content': input_query},
        ],
        stream=True,
    )

    print('Chatbot response:')
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
