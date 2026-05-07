def router(state):

    query = state.get("query", "").lower()

    if any(word in query for word in [
        "diabetes",
        "health",
        "doctor",
        "medicine",
        "blood",
        "diet"
    ]):
        return {
            "route": "healthcare"
        }

    elif any(word in query for word in [
        "stock",
        "finance",
        "investment",
        "crypto",
        "money"
    ]):
        return {
            "route": "finance"
        }

    elif any(word in query for word in [
        "python",
        "code",
        "bug",
        "api",
        "programming"
    ]):
        return {
            "route": "coding"
        }

    return {
        "route": "general"
    }