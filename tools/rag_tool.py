import chromadb
from sentence_transformers import SentenceTransformer
from config import DB_DIR, COLLECTION_NAME, EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

client = chromadb.PersistentClient(path=DB_DIR)
collection = client.get_collection(COLLECTION_NAME)


def search_building_docs(question: str, n_results: int = 4) -> str:
    """
    Search Ontario permit/building documents and return relevant context.
    This will later become an agent tool.
    """

    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context_blocks = []

    for doc, meta in zip(documents, metadatas):
        context_blocks.append(
            f"Source: {meta['source']}, Page: {meta['page']}\n{doc}"
        )

    return "\n\n---\n\n".join(context_blocks)