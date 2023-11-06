import numpy as np
import faiss

DIMENSIONS = 1280  # Update to match your embeddings' dimensions
INDEX_FILE_PATH = 'databank/faiss_index.index'

index = faiss.IndexFlatL2(DIMENSIONS)
index = faiss.IndexIDMap(index)

try:
    index = faiss.read_index(INDEX_FILE_PATH)
except:
    print("Failed to load existing index. A new index will be created.")

def add_item_to_index(item_vector,id):
    item_vector = np.array(item_vector).astype('float32')
    index.add_with_ids(np.array([item_vector]),[id])
    faiss.write_index(index, INDEX_FILE_PATH)

def get_similar_items(item_vector, num_matches=5):
    item_vector = np.array(item_vector).astype('float32')
    distances, indices = index.search(np.array([item_vector]), num_matches)
    return indices[0]

def remove_item_with_id(id):
    # ids_to_remove_array=np.array(,dtype=np.int64)
    index.remove_ids([id])
    faiss.write_index(index,'index.faiss')
