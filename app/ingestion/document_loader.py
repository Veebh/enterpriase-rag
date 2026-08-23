from pathlib import Path

DOCUMENTS_PATH = Path("data/documents")

def load_documents():
    documents = []

    for file_path in DOCUMENTS_PATH.rglob("*.txt"):

        text = file_path.read_text(encoding="utf-8")

        department = file_path.parent.name

        documents.append(
            {
                "text" : text,
                "source" : str(file_path),
                "file_name": file_path.name,
                "department": department
            }
        )

    return documents