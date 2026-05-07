from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import os


DOCS_PATH = "data/docs"
DB_PATH = "vectorstore"


def load_documents():
    documents = []

    for file in os.listdir(DOCS_PATH):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(DOCS_PATH, file)

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            documents.extend(docs)

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


def create_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    vectorstore.persist()

    print("✅ Vector DB created")


if __name__ == "__main__":

    print("🚀 Loading PDFs...")

    docs = load_documents()

    print(f"Loaded {len(docs)} pages")

    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    create_vectorstore(chunks)