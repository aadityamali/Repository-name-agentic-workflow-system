from transformers import pipeline


pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)


def generator(state):

    query = state.get("query", "")
    context = state.get("context", "")

    prompt = f"""
Context:
{context}

Question:
{query}

Answer:
"""

    result = pipe(
        prompt,
        max_new_tokens=100
    )

    answer = result[0]["generated_text"]

    return {
        "answer": answer
    }