class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        check = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in check:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    ch = stack.pop()
                    if check.get(ch)!=char:
                        return False
        return not stack
        