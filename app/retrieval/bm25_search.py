from rank_bm25 import BM25Okapi

from app.ingestion.chunker import chunk_document
from app.ingestion.document_loader import load_documents

documents = load_documents()

all_chunks = []

for document in documents:

    chunks = chunk_document(document)

    all_chunks.extend(chunks)

tokenized_chunks = [
    chunk.chunk_text.lower().split()
    for chunk in all_chunks
]

bm25 = BM25Okapi(tokenized_chunks)

def search_bm25(query:str, top_k=5):
    tokenized_query = query.lower().split()

    scores = bm25.get_scores(tokenized_query)

    ranked_indexes = sorted(range(len(scores)),
                            key= lambda index: scores[index],
                            reverse=True
                            )[:top_k]
    results = []

    for index in ranked_indexes:

        chunk = all_chunks[index]

        results.append(
            {
            "text": chunk.chunk_text,
            "score": float(scores[index]),
            "source" : chunk.source,
            "file_name" : chunk.file_name,
            "department" : chunk.chunk_dept,
            "chunk_index": chunk.chunk_index
        }
        )

        return results