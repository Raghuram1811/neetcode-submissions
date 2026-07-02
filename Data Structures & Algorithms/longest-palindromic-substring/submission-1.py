class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        max_string = ""

        for idx in range(len(s)-1):
            odd = self.expandFromCenter(s, idx, idx+1)
            even = self.expandFromCenter(s, idx, idx)
            if len(max_string) < len(odd):
                max_string = odd
            if len(max_string) < len(even):
                max_string = even
        return max_string

    def expandFromCenter(self, s: str, start: int, end: int) -> str:

        while start>=0 and end < len(s) and s[start]==s[end]:
            start-=1
            end+=1
        return s[start+1: end]