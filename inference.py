from server.cloud_env import CloudEnv

env = CloudEnv()
state = env.reset()

total_reward = 0
scores = {"easy": 0, "medium": 0, "hard": 0}

for i in range(100):
    cpu = state["cpu_usage"]
    servers = state["servers"]
    requests = state["requests"]

    # Smart logic: aim for CPU 40-70% with servers ≤ 3
    target_cpu = 55  # sweet spot (middle of 40-70)

    if cpu > 70 and servers < 3:
        action = "scale_up"
    elif cpu > 80:
        action = "scale_up"
    elif cpu < 40 and servers > 1:
        action = "scale_down"
    else:
        action = "do_nothing"

    state, reward, done, _ = env.step(action)
    total_reward += reward

    # Track scores
    if 40 <= state["cpu_usage"] <= 70:
        scores["easy"] += 1
    if state["cpu_usage"] < 80 and state["servers"] <= 3:
        scores["medium"] += 1
    if 40 <= state["cpu_usage"] <= 70 and state["servers"] <= 3:
        scores["hard"] += 1

    print(f"Step {i}: CPU={state['cpu_usage']:.1f}% | "
          f"Servers={state['servers']} | Reward={reward}")

print(f"\n{'='*40}")
print(f"Total Reward: {total_reward}")
print(f"Scores: {scores}")
print(f"Hard Score Rate: {scores['hard']/100*100:.1f}%")