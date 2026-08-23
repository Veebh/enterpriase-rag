
from qdrant_client.models import Distance, PointStruct, VectorParams
from qdrant_client import QdrantClient

from app.embeddings.embedding_model import generate_embedding
from app.ingestion.chunker import chunk_document
from app.ingestion.document_loader import load_documents


COLLECTION_NAME = "enterprise_documents"

client = QdrantClient(
    url='http://localhost:6333'
)


if client.collection_exists(collection_name=COLLECTION_NAME):
    client.delete_collection(COLLECTION_NAME)

client.create_collection(
    collection_name = COLLECTION_NAME,
    vectors_config=VectorParams(
        size = 384,
        distance = Distance.COSINE
    )
)

print("Collection created successfully.")
documents = load_documents()

points = []
point_id = 1

for document in documents:
    chunks = chunk_document(document)

    for chunk in chunks:

        vector = generate_embedding(chunk.chunk_text)

        point = PointStruct(
            id= point_id,
            vector = vector.tolist(),

            payload = {
                "text" : chunk.chunk_text,
                "source" : chunk.source,
                "file_name" : chunk.file_name,
                "department" : chunk.chunk_dept,
                "chunk_index" : chunk.chunk_index
            }
        )

        points.append(point)
        point_id = point_id+1


client.upsert(
    collection_name=COLLECTION_NAME,
    points = points
)

print(f"Inserted {len(points)} chunks into Qdrant.")