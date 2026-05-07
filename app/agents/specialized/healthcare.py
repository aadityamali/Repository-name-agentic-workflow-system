def healthcare_agent(state):

    query = state.get("query", "")

    return {
        "specialist_response": f"Healthcare Agent handled: {query}"
    }