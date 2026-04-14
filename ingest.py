import os
import argparse
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

def ingest_maritime_pdfs(file_path, index_name):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    loader = UnstructuredPDFLoader(
        file_path, 
        strategy="hi_res",  
        mode="elements"     
    )
    
    raw_docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    
    chunks = text_splitter.split_documents(raw_docs)
    cleaned_chunks = []
    for chunk in chunks:
        source = os.path.basename(file_path)
        page = chunk.metadata.get("page_number", "Unknown")

        chunk.metadata = {
            "source": str(source),
            "page_number": str(page)
        }
        cleaned_chunks.append(chunk)

    PineconeVectorStore.from_documents(
        cleaned_chunks,
        embeddings,
        index_name=index_name
    )
    print(f"Successfully ingested {len(cleaned_chunks)} chunks from {file_path}")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Ingest one or more PDFs into Pinecone")
    parser.add_argument("files", nargs="+", help="PDF file paths to ingest")
    parser.add_argument(
        "--index",
        default=os.getenv("SHIPAI_INDEX_NAME", "shipdata"),
        help="Pinecone index name (default: SHIPAI_INDEX_NAME or shipdata)",
    )
    args = parser.parse_args()

    for file_path in args.files:
        ingest_maritime_pdfs(file_path, args.index)


if __name__ == "__main__":
    main()