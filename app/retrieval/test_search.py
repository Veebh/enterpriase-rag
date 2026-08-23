from asyncio import sleep

from app.retrieval.semantic_search import search

while True:
    query = input("ask user query: ")


    print(f'\n Query : {query}')

    searchResults = search(query)
    

    print('\n Results')

    for index, result in enumerate(searchResults):

        print("\n==============================")

        print("Rank:", index + 1)
        print("Score:", round(result["score"], 4))
        print("File:", result["file_name"])
        print("Department:", result["department"])

        print("\nText:")
        print(result["text"])