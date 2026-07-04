class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] < 9:
            digits[-1]+=1
            return digits
        
        else:
            string, value = "", ""
            for idx in range(len(digits)):
                string+=str(digits[idx])
                value = str(int(string)+1)
            return [int(i) for i in value]
