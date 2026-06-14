# knowledge/retrieval.py

from sentence_transformers import CrossEncoder

from knowledge.chroma_store import architecture_collection, incident_collection

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")


def rerank_results(query, chunks):

    pairs = [
        (query, chunk)
        for chunk in chunks
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(scores, chunks),
        reverse=True
    )

    return [
        doc
        for _, doc in ranked[:3]
    ]


def retrieve_dependencies(
    service_name
):

    print(
        "Architecture Collection Count:",
        architecture_collection.count()
    )
    results = architecture_collection.query(
        query_texts=[service_name],
        n_results=5
    )
    

    docs = results["documents"][0]

    docs = [
        doc
        for doc in docs
        if doc and doc.strip()
    ]

    if len(docs) == 0:
        return []

    return rerank_results(
        service_name,
        docs
    )

def retrieve_incidents(service_name):
    print(
        "Incident Collection Count:",
        incident_collection.count()
    )

    results = incident_collection.query(
        query_texts=[service_name],
        n_results=10
    )

    docs = results["documents"][0]

    docs = [
        doc
        for doc in docs
        if doc and doc.strip()
    ]

    if len(docs) == 0:
        return []

    return rerank_results(
        service_name,
        docs
    )