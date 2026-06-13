from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from app.services.embedding_service import get_embedding_model
from app.rag.text_splitter import split_text

def build_resume_vector_store(resume_text: str):
    chunks = split_text(resume_text)

    documents = [
        Document(page_content=chunk, metadata={"source": "resume"})
        for chunk in chunks
    ]

    embeddings = get_embedding_model()
    return FAISS.from_documents(documents, embeddings)

def search_resume_matches(resume_text: str, job_description: str, top_k: int = 3):
    vector_store = build_resume_vector_store(resume_text)
    jd_chunks = split_text(job_description)

    matched_chunks = []

    for chunk in jd_chunks:
        results = vector_store.similarity_search_with_score(chunk, k=top_k)

        for document, score in results:
            matched_chunks.append({
                "job_requirement": chunk,
                "resume_match": document.page_content,
                "distance": float(score),
            })

    return matched_chunks