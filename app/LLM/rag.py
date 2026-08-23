

from app.LLM.contextbuilder import build_context
from app.LLM.llm import generate_answer
from app.LLM.prompt import SYSTEM_PROMPT
from app.retrieval.rag_retriever import do_rag_retrieve


def ask_question(question: str):

    #1 .Retrieve Relavant Chunks
    results = do_rag_retrieve(query=question,
                              candidate_k=20,
                              top_k=5)

    #2. Build context
    context = build_context(results)

    #3. Build prompt
    prompt = SYSTEM_PROMPT.format(context=context,question=question)

    #4. Ask LLM
    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "sources":results
    }



        
