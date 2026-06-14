from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from knowledge.chroma_store import architecture_collection, incident_collection
from knowledge.document_loader import load_document

SUPPORTED_PATTERNS = [
    "*.pdf",
    "*.txt",
    "*.md",
    "*.yaml",
    "*.yml",
    "*.json",
    "*.csv"
]


def chunk_text(
        text,
        chunk_size=1000,
        chunk_overlap=200
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    return splitter.split_text(text)


def ingest_folder(
        folder_path,
        collection
):

    folder = Path(folder_path)

    files = []

    for pattern in SUPPORTED_PATTERNS:
        files.extend(
            folder.glob(pattern)
        )

    print(
        f"\nScanning Folder: {folder_path}"
    )

    print(
        f"Files Found: {len(files)}"
    )

    total_chunks = 0

    for file in files:

        print(
            f"\nProcessing: {file.name}"
        )

        try:

            text = load_document(
                file
            )

            if not text.strip():

                print(
                    f"Skipping empty file: {file.name}"
                )

                continue

            chunks = chunk_text(text)

            collection.add(
                documents=chunks,
                ids=[
                    f"{file.stem}_{i}"
                    for i in range(
                        len(chunks)
                    )
                ],
                metadatas=[
                    {
                        "source": file.name,
                        "file_type": file.suffix
                    }
                    for _ in chunks
                ]
            )

            total_chunks += len(chunks)

            print(
                f"Added {len(chunks)} chunks"
            )

        except Exception as e:

            print(
                f"Failed to process {file.name}"
            )

            print(str(e))

    print(
        f"\nTotal Chunks Added: {total_chunks}"
    )


def ingest_all():

    print(
        "\n========== INGESTION STARTED =========="
    )

    ingest_folder(
        "./data/architecture_docs",
        architecture_collection
    )

    ingest_folder(
        "./data/incident_docs",
        incident_collection
    )

    print(
        "\n========== COLLECTION STATS =========="
    )

    print(
        "Architecture Count:",
        architecture_collection.count()
    )

    print(
        "Incident Count:",
        incident_collection.count()
    )

    print(
        "\n========== INGESTION COMPLETE =========="
    )


if __name__ == "__main__":

    ingest_all()