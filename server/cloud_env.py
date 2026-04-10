import random


class CloudEnv:
    def __init__(self):
        self.cpu = 50
        self.servers = 2
        self.requests = 100
        self.reset()

    def reset(self):
        self.cpu = 50
        self.servers = 2
        self.requests = 100
        return self.state()

    def state(self):
        return {
            "cpu_usage": self.cpu,
            "servers": self.servers,
            "requests": self.requests
        }

    def step(self, action):
        # Handle action
        if action == "scale_up":
            self.servers += 1
        elif action == "scale_down" and self.servers > 1:
            self.servers -= 1

        # Simulate traffic change
        self.requests += random.randint(-20, 30)
        self.requests = max(1, self.requests)  # Prevent 0 or negative requests

        # Calculate CPU usage
        self.cpu = round(self.requests / (self.servers * 2), 2)

        # Calculate reward
        reward = self.calculate_reward()

        return self.state(), reward, False, {}

    def calculate_reward(self):
        if self.cpu > 90:
            return -1
        elif self.cpu > 80:
            return -0.5
        elif self.cpu < 30:
            return -0.5
        elif 40 <= self.cpu <= 70:
            return 2
        else:
            return 1