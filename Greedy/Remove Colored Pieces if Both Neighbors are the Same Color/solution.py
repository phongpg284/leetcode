class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = sum((len(num) - 2) for num in colors.split("B") if len(num) > 2 )
        bob = sum((len(num) - 2)  for num in colors.split("A") if len(num) > 2)
        return alice > bob 