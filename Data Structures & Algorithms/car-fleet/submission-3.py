class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Sorting position list with zipped speed - Very imp step to identify the cars at closest position to target. Gives cars closest to farthest list[a, b, c, d] a is closest to target

        zipped = sorted(list(zip(position, speed)), reverse = True)
        stack = deque()
        for pos, sp in zipped:
            time = (target-pos)/sp
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)