class Solution:
    def isValid(self, s: str) -> bool:
        check = {'{': '}', '(': ')', '[':']'}
        stack = deque([])

        for char in s:
            if char in check:
                stack.append(char)
            else:
                if not stack:
                    return False
                ch = stack.pop()
                if char!=check.get(ch):
                    return False
        return len(stack)==0