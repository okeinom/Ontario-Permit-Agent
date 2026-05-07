from pathlib import Path
from pypdf import PdfReader
import chromadb
from sentence_transformers import SentenceTransformer
from config import DB_DIR, COLLECTION_NAME, PDF_DIR, EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

client = chromadb.PersistentClient(path=DB_DIR)
collection = client.get_or_create_collection(COLLECTION_NAME)


def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def ingest_pdfs():
    doc_id = 0

    for pdf_path in Path(PDF_DIR).glob("*.pdf"):
        reader = PdfReader(str(pdf_path))

        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            if not text.strip():
                continue

            chunks = chunk_text(text)

            for chunk_index, chunk in enumerate(chunks):
                embedding = model.encode(chunk).tolist()

                collection.upsert(
                    ids=[f"{pdf_path.stem}-p{page_num}-c{chunk_index}"],
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[{
                        "source": pdf_path.name,
                        "page": page_num,
                        "chunk_index": chunk_index
                    }]
                )

                doc_id += 1

    print(f"Ingested {doc_id} chunks.")


if __name__ == "__main__":
    ingest_pdfs()