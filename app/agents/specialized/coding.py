def coding_agent(state):

    query = state.get("query", "")

    return {
        "specialist_response": f"Coding Agent handled: {query}"
    }