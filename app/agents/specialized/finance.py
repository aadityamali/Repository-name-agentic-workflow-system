def finance_agent(state):

    query = state.get("query", "")

    return {
        "specialist_response": f"Finance Agent handled: {query}"
    }