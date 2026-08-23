
from app.embeddings.embedding_model import generate_embedding
from app.ingestion.document_loader import load_documents
from app.ingestion.chunker import chunk_document, chunk_text

documents = load_documents()

print(f"Documents found: {len(documents)}")

for document in documents:

    print("\n____________________")
    print(f"File: {document["file_name"]} ")
    print("Department",document["department"])
    print("Source",document["source"])


    chunks = chunk_document(document)

    print(f"number of chunks {len(chunks)}")

    for chunk in chunks:
        print(f"\n Chunk id: {chunk.chunk_id} \n Chuni index: {chunk.chunk_index} \n \n Chunk Text: {chunk.chunk_text}")

        embedding = generate_embedding(chunk.chunk_text)

        print(f"vector type {type(embedding)}")
        print(f"vector dimenstions {len(embedding)}")
        print("\n First 10 vector values")
        print(embedding[:10])
    # chunks = chunk_text(document["text"])

    # print("CHUNKS: ",len(chunks))

    # for index,chunk in  enumerate(chunks):
    #     print(f"\n------------------------------------ chunk index: {index}------------------------------------------------------\n")
    #     print(chunk)

    # print("\nText")
    # print(document["text"][:200])
