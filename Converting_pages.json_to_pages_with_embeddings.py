import json
import openai
import os
import tqdm

# Set up OpenAI API key
openai.api_key = "You_OpenAI_API_key"

# Define model and parameters
model_engine = "text-embedding-ada-002"

with open('pages.json') as f:
    pages = json.load(f)
    for i, page in enumerate(pages):
        # Generate embeddings
        response = openai.Embedding.create(
            model=model_engine,
            input=page['page']
        )
        # Extract embeddings from response
        embedding = response["data"][0]["embedding"]
        # Add the embeddings to the pages array
        pages[i]['embedding'] = embedding

with open('pages_with_embeddings.json', 'w') as f:
    json.dump(pages, f)
