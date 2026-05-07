from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


DB_PATH = "vectorstore"


# embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# load vector DB
vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)


# create retriever
retriever_db = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


def retriever(state):

    query = state.get("query", "")

    # ✅ FIXED
    docs = retriever_db.invoke(query)

    context = "\n\n".join([
    doc.page_content[:500].replace("\n", " ")
    for doc in docs
])

    return {
        "context": context
    }