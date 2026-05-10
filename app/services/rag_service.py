from langchain_openai import ChatOpenAI

from app.schemas.ask import AskResponse, SourceResponse
from app.services.retrieval_service import search_similar_chunks


def ask_trip_documents(trip_id: str, question: str) -> AskResponse:
    retrieved_docs = search_similar_chunks(
        trip_id=trip_id,
        question=question,
        k=4
    )

    if not retrieved_docs:
        return AskResponse(
            question=question,
            answer="I could not find relevant information in your uploaded trip documents.",
            sources=[]
        )

    context = "\n\n---\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are TripMind AI, a helpful travel assistant.

Answer the user's question using ONLY the provided context from uploaded travel documents.

Rules:
- Do not invent information.
- If something is not mentioned in the context, say that it is not available in the uploaded documents.
- Be practical and concise.
- Mention places, routes, food, transport, or budget only if they appear in the context.
- Return a clean answer for a traveller.

CONTEXT:
{context}

QUESTION:
{question}
"""

    llm = ChatOpenAI(
        model="gpt-5.4-nano",
        temperature=0.5
    )

    response = llm.invoke(prompt)

    sources = []

    for doc in retrieved_docs:
        metadata = doc.metadata

        sources.append(
            SourceResponse(
                filename=metadata.get("filename", "unknown"),
                chunk_index=metadata.get("chunk_index", -1)
            )
        )

    return AskResponse(
        question=question,
        answer=response.content,
        sources=sources
    )