from app.retrieval.bm25_search import search_bm25
from app.retrieval.semantic_search import search


def reciprocal_rank_fusion(vector_results, bm25_results, k=60):
    combined = {}

    for rank, result in enumerate(vector_results, start=1):

        key = (result['file_name'],result['chunk_index'])

        combined.setdefault(
            key,
            {
                "result":result,
                "rrf_score": 0
            }
        )
        combined[key]["rrf_score"] += (1/(rank+k))

    for rank, result in enumerate(bm25_results, start=1) :

        key = (result['file_name'],result['chunk_index'])
        
        combined.setdefault(
            key,
            {
                "result":result,
                "rrf_score": 0
            }
        )
        combined[key]["rrf_score"] += (1/(rank+k))

    ranked = sorted(
        combined.values(),
        key=lambda result:result['rrf_score'],
        reverse = True)

    results = []

    for item in ranked:
        result = item["result"].copy()
        result['rrf_score'] = item['rrf_score']
        results.append(result)

    return results

def do_hybrid_search(query, top_k = 5):
    vector_results = search(query,top_k)
    bm25_results = search_bm25(query,top_k)
    return reciprocal_rank_fusion(vector_results=vector_results,bm25_results=bm25_results,k=60)[:top_k]