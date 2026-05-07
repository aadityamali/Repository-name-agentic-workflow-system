def planner(state):
    query = state["query"]

    plan = f"""
    Plan:
    1. Understand the query: {query}
    2. Retrieve relevant knowledge
    3. Generate a structured answer
    """

    return {"plan": plan}