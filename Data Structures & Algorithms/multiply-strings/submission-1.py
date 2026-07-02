class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        num1 = self.stringToInt(num1)
        num2 = self.stringToInt(num2)
        
        return str(num1*num2)

    def stringToInt(self, s: str) -> int:

        power, value = 0, 0
        for idx in range(len(s)-1, -1, -1):
            value+=int(s[idx])*(10**power)
            power+=1
        return value
