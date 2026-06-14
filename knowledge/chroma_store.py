import chromadb
from knowledge.embeddings import embedding_fn


client = chromadb.PersistentClient(path="./chroma_db")

architecture_collection = (
    client.get_or_create_collection(
        name="architecture_docs",
        embedding_function=embedding_fn
    )
)

incident_collection = (
    client.get_or_create_collection(
        name="incident_docs",
        embedding_function=embedding_fn
    )
)