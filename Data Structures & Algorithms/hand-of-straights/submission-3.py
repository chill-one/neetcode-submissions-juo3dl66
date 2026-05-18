class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
    
        """
        [1,2,4,2,3,5,3,4]
        [1,2,2,3,3,4,4,5]
        """

        freq = Counter(hand)
        sorted_keys = sorted(freq.keys())

        for h in sorted_keys:
            if freq[h] > 0:
                count_to_remove = freq[h]
                for i in range(groupSize):
                    target = h + i
                    if freq[target] < count_to_remove:
                        return False
                    freq[h + i] -= count_to_remove


        return True

