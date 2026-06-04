class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
            
        stones = sorted(stones, reverse=True)
        stones[0]-=stones[1]
        stones.pop(1)
        return self.lastStoneWeight(stones)