from dataclasses import dataclass

@dataclass
class DocumentChunk:
    chunk_id:str
    chunk_text:str

    chunk_dept:str
    source:str
    file_name:str

    chunk_index:int