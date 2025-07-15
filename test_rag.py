from rag import load_kb, get_answer

questions, kb = load_kb("data/faqs.txt")
query = "I need help with my password"
response = get_answer(query, questions, kb)
print("Answer:", response)
