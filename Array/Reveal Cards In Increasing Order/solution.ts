function deckRevealedIncreasing(deck: number[]): number[] {
  deck.sort((a, b) => a - b);
  let result = [];
  helper(deck, result);
  return result;
}

function helper(deck, result = []) {
  if (!deck.length) return;
  if (result.length) result.unshift(result.pop());
  result.unshift(deck.pop());
  helper(deck, result);
}
