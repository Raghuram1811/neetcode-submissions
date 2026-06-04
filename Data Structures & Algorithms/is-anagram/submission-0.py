class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = dict()
        for ch in s:
            check[ch] = check.get(ch, 0)+1
        for ch in t:
            check[ch] = check.get(ch, 0)-1
        
        for ch in check:
            if check[ch]:
                return False
        return True