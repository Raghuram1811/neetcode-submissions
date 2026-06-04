class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sortedS = ''.join(sorted(string))
            result[sortedS].append(string)
        return list(result.values())

