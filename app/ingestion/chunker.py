from app.ingestion.model.chunk import DocumentChunk
from pathlib import Path

def chunk_document(document,chunk_size=500,overlap=100):
    text = document["text"]

    chunks = []
    start = 0
    index = 0

    while start < len(text):

        end = start + chunk_size
        chunk_text = text[start:end].strip()

        if chunk_text:

            chunk_id = f"{document["department"]}_ {Path(document["file_name"]).stem}_{index}"

            chunk = DocumentChunk(
                chunk_id=chunk_id,
                chunk_text = chunk_text,
                source = document["source"],
                chunk_dept=document["department"],
                file_name=document["file_name"],
                chunk_index=index
            )

            chunks.append(chunk)

            index = index+1
        start = end - overlap

    return chunks


def chunk_text(text,chun_size=500,overlap=100):
    chunks = []

    start = 0

    while(start < len(text)):
        end = start + chun_size

        chunk = text[start:end]

        chunks.append(chunk.strip())

        start = end - overlap

    return chunks



