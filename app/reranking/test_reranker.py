

from app.reranking.reranker import do_reranking
from app.retrieval.hybrid_search import do_hybrid_search


while True:

    query = input("ask your question:")

    documents = do_hybrid_search(query,top_k=10)

    print("\nBEFORE RERANKING")

    for index, result in enumerate(documents):
        print(
            index + 1, result["file_name"],
            result["rrf_score"]
        )

    rerankedDocuments = do_reranking(query,documents=documents,top_k=5)

    for index, result in enumerate(rerankedDocuments):
        print(index+1,result['file_name'],result['reranker_score'])

