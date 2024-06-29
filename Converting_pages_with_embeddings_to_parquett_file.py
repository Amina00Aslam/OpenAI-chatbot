import pyarrow as pa
import pyarrow.parquet as pq
import json

# Load the embedded file data
with open('pages_with_embeddings.json', 'r') as f:
    embedded_data = json.load(f)

# Create separate lists for each column
chapters = [page['chapter'] for page in embedded_data]
pages = [page['page'] for page in embedded_data]
page_numbers = [page['page_number'] for page in embedded_data]
embeddings = [page['embedding'] for page in embedded_data]

# Convert the data to PyArrow arrays
chapter_array = pa.array(chapters)
page_array = pa.array(pages)
page_number_array = pa.array(page_numbers)
embedding_array = pa.array(embeddings)

# Create a PyArrow Table from the arrays
table = pa.Table.from_arrays([chapter_array, page_number_array, page_array, embedding_array],
                             names=['chapter', 'page_number', 'page', 'embedding'])

# Write the PyArrow Table to a Parquet file
output_file = 'embedded_data.parquet'
pq.write_table(table, output_file)
