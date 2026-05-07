from fastapi import FastAPI

from app.graph import graph


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Agentic Workflow System Running"
    }


@app.post("/run")
def run_agent(query: str):

    result = graph.invoke({
        "query": query
    })

    return result