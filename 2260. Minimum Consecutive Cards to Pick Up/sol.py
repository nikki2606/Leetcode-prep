class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minLen = float('inf')
        window_size = 0
        unique_cards = set()
        for i in range(len(cards)):
            window_size += 1
            while cards[i] in unique_cards:
                minLen = min(minLen, window_size)
                unique_cards.remove(cards[i-window_size+1])
                window_size -= 1
            unique_cards.add(cards[i])
            
        return minLen if minLen != float('inf') else -1