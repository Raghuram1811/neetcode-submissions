class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        check = {'(': ')', '{': '}', '[': ']'}
        
        for ch in s:
            if ch in check:
                stack.append(ch)
            else:
                if not stack:
                    return False
                char = stack.pop()
                if ch!=check.get(char):
                    return False
        return not stack
                                                                                                                                                                                                                                              