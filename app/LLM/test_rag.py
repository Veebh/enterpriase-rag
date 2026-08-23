

from app.LLM.rag import ask_question


while True:

    question = input("ask your question :")

    result = ask_question(question = question)

    print("\n QUESTION: ")
    print(question)

    print("\n answer: ")
    print(result['answer'])

    print("\n sources: ")

    for source in result['sources']:
        print(f"{source['file_name']} score {source['reranker_score']}")