

from app.reranking.reranker import do_reranking
from app.retrieval.hybrid_search import do_hybrid_search


def do_rag_retrieve(query,candidate_k=20,top_k=5):
    candidates = do_hybrid_search(query,top_k=candidate_k)
    results = do_reranking(
        query=query,
        documents=candidates,
        top_k=top_k)
    return results

