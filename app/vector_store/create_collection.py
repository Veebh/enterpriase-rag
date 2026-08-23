from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(
    url='http://localhost:6333'
)


COLLECTION_NAME = "enterprise_documents"

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
