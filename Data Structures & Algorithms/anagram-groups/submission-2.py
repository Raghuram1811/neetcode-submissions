class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []

        check = collections.defaultdict(list)
        for string in strs:
            key = sorted(string)
            check[tuple(key)].append(string)
        
        return [i for i in check.values()]