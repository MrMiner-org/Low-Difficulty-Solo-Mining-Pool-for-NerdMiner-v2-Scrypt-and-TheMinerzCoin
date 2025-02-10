import time

class RateLimiter:
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit
        self.last_time = time.time()
        self.allowance = rate_limit

    def allow_request(self):
        current = time.time()
        elapsed = current - self.last_time
        self.last_time = current
        self.allowance += elapsed * self.rate_limit
        if self.allowance > self.rate_limit:
            self.allowance = self.rate_limit
        if self.allowance < 1.0:
            return False
        else:
            self.allowance -= 1.0
            return True
