from asyncio import sleep

from app.retrieval.bm25_search import search_bm25

while True:
    query = input("ask user query: ")


    print(f'\n Query : {query}')

    searchResults = search_bm25(query)
    

    print(f'\n Results : {str(len(searchResults))}')

    for index, result in enumerate(searchResults):

        print("\n==============================")

        print("Rank:", index + 1)
        print("Score:", round(result["score"], 4))
        print("File:", result["file_name"])
        print("Department:", result["department"])

        print("\nText:")
        print(result["text"])