class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemies = sorted(enemyEnergies)
        if currentEnergy < enemies[0]:
            return 0

        return (sum(enemies) - enemies[0] + currentEnergy) // enemies[0]
