

from sentence_transformers import CrossEncoder


MODEL_NAME = 'BAAI/bge-reranker-base'

model = CrossEncoder(MODEL_NAME)

def do_reranking(query,documents,top_k=5):
    pairs = []

    for document in documents:
        pairs.append(
            (
                query,document['text']
            )
        )

    scores = model.predict(pairs)

    reranked_documets = []

    for document,score in zip(documents,scores):

        result = document.copy()
        result['reranker_score'] = score

        reranked_documets.append(result)


    reranked_documets.sort(
        key= lambda reranked_document:reranked_document['score'],
        reverse=True
    )

    return reranked_documets[:top_k]

