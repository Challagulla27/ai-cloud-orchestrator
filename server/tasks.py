def easy_task(state):
    cpu = state["cpu_usage"]
    if 40 <= cpu <= 70:
        return 1
    elif 30 <= cpu <= 80:
        return 0.5    # Close but not perfect
    return 0


def medium_task(state):
    cpu = state["cpu_usage"]
    servers = state["servers"]
    score = 0
    if cpu < 80:
        score += 0.5
    if servers <= 3:
        score += 0.5
    return score


def hard_task(state):
    cpu = state["cpu_usage"]
    servers = state["servers"]

    if 40 <= cpu <= 70 and servers <= 3:
        return 1
    elif 40 <= cpu <= 70 and servers > 3:
        return 0.5
    elif cpu < 80 and servers <= 3:
        return 0.3
    return 0