from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load Q&A and build FAISS index
def load_kb(file_path='data/faqs.txt'):
    with open(file_path, 'r') as f:
        blocks = f.read().strip().split('\n\n')
    kb = []
    for block in blocks:
        try:
            q_line, a_line = block.strip().split('\n')
            question = q_line[3:].strip()  
            answer = a_line[3:].strip()    
            kb.append((question, answer))
        except:
            continue
    questions = [q for q, _ in kb]
    return questions, kb

# Retrieve best answer using cosine similarity
def get_answer(query, questions, kb):
    question_embeddings = model.encode(questions)
    query_embedding = model.encode([query])

    # Convert to numpy arrays
    question_embeddings = np.array(question_embeddings).astype("float32")
    query_embedding = np.array(query_embedding).astype("float32")

    # Create FAISS index
    index = faiss.IndexFlatL2(question_embeddings.shape[1])
    index.add(question_embeddings)

    # Search for closest question
    _, I = index.search(query_embedding, 1)
    best_match_idx = I[0][0]
    top_q, top_a = kb[best_match_idx]
    return top_a
