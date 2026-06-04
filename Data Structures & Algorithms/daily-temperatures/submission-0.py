class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        
        result = [0]*len(temperatures)

        for idx in range(len(temperatures)):
            for jdx in range(idx+1, len(temperatures)):
                if temperatures[jdx]>temperatures[idx]:
                    result[idx] = jdx-idx
                    break
        return result
