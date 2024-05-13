class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        s = [-1] * n
        for i in range(n - 1, -1, -1):
            s[i] = s[i + k] + energy[i] if i + k < n else energy[i]
        return max(s)
