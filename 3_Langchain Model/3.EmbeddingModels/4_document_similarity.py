from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Load embedding model
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Define documents and query
documents = [
    "Virat Kholi is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is calm and composed captain who mastered the art of finishing games under pressure.",
    "Rohit Sharma is Hitman of Indian cricket, famous for his effortless sixes and double centuries.",
    "Jasprit Bumrah is India’s yorker king, delivering deadly precision at crucial moments.",
    "Sachin Tendulkar is legendary God of Cricket who inspired generations with his iconic career."
]

query = "Tell me about Virat Kholi"

# Compute embeddings
doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Compute cosine similarity
scores = cosine_similarity([query_embedding], doc_embedding)[0]

# Get the index and score of the most similar document
index = np.argmax(scores)
score = scores[index]

# Print results
print("Query:", query)
print("Most Similar Document:", documents[index])
print("Similarity Score:", score)
