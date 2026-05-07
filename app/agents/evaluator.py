def evaluator(state):
    answer = state["answer"]

    if answer and len(answer) > 20:
        return {"evaluation": "valid"}
    else:
        return {"evaluation": "invalid"}