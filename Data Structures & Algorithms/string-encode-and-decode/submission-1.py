class Solution:

    def __init__(self):
        self.check_map = {}

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+=str(len(string))+"#"+string
        self.check_map[res] = strs
        return res


    def decode(self, s: str) -> List[str]:
        return self.check_map[s]
