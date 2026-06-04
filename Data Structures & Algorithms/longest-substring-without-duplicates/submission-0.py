class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for idx in range(len(s)):
            charset = set()
            for jdx in range(idx, len(s)):
                if s[jdx] in charset:
                    break
                charset.add(s[jdx])
            result = max(result, len(charset))
        return result