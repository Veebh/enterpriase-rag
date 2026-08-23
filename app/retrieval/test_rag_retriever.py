from app.retrieval.rag_retriever import do_rag_retrieve


while True:
    query = input('ask your question: ')

    results = do_rag_retrieve(query=query)



    print("\nQUERY:")
    print(query)


    for index, result in enumerate(results):

        print("\n==============================")

        print("Rank:", index + 1)

        print(
            "Rerank Score:",
            round(result["reranker_score"], 4)
        )

        print(
            "File:",
            result["file_name"]
        )

        print(
            "Department:",
            result["department"]
        )

        print("\nTEXT:")
        print(result["text"])