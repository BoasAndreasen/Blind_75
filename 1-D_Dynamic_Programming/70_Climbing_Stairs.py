class Solution:
    def __init__(self):
        self.d = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        else:
            self.d[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.d[n]
