
from app.LLM.llm import generate_answer

prompt = """
What is RAG?
Explain it in two sentences.
"""

answer = generate_answer(prompt)

print(answer)