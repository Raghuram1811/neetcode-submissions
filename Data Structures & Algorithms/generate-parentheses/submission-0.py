class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        ans = []

        def check(string):

            stack = []
            check = {'(': ')'}

            for ch in string:
                if ch in check:
                    stack.append(ch)
                else:
                    if not stack:
                        return False
                    char = stack.pop()
                    if check[char]!=ch:
                        return False
            return not stack

        def backtrack(curr_str):
            if len(curr_str) == 2 * n:
                if check(curr_str):
                    ans.append(curr_str)

                return  # Must return whether valid or invalid

            backtrack(curr_str + "(")
            backtrack(curr_str + ")")

        backtrack("")
        return ans
            
