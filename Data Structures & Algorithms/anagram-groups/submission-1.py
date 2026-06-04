class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        response = []

        check = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            check[sorted_string].append(string)
        return list(check.values())
        