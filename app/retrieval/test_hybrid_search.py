 


from app.retrieval.hybrid_search import do_hybrid_search


while True:
    query = input("Enter your query: ")

    results = do_hybrid_search(query)

    print(f"query: {query}")

    for index, result in enumerate(results):
        print("\n =======================================================")

        print("\n Rank ", index+1)

        print("\n RRF Score",round(result['rrf_score'],6))
        print("\n File ",result['file_name'])
        print("\n Department ", result['department'])
        print("\n Text:",result['text'])
