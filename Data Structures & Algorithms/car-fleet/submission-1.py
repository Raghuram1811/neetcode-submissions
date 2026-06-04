class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        zipped = list(zip(position, speed))
        zipped.sort(reverse=True)
        stack = []
        for pos, sp in zipped:
            residue = (target - pos)/sp
            stack.append(residue)
            if len(stack)>=2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)
