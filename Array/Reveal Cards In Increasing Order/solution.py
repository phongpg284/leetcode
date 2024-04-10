class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        result = deque()
        self.helper(deck, result)
        return result

    def helper(self, deck, result):
        if not deck:
            return
        if result:
            result.appendleft(result.pop())
        result.appendleft(deck.pop())
        self.helper(deck, result)
