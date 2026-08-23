from qdrant_client import QdrantClient

from app.embeddings.embedding_model import generate_embedding

COLLECTION_NAME ='enterprise_documents'

client = QdrantClient(
    url='http://localhost:6333'
)

def search(text: str, top_k= 5):

    query_vector = generate_embedding(text)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query = query_vector.tolist(),
        limit= top_k,
        with_payload=True
    )
    
    formatted_results = []

    for result in results.points:

        formatted_results.append({
            "score": result.score,
            "text": result.payload["text"],
            "source": result.payload["source"],
            "file_name": result.payload["file_name"],
            "department": result.payload["department"],
            "chunk_index": result.payload["chunk_index"]
        })

    return formatted_results

