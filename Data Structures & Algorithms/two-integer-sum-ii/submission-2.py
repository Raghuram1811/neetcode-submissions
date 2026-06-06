class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for idx in range(len(numbers)):
            left, right = idx+1, len(numbers)-1

            temp = target - numbers[idx]
            
            while left<=right:
                middle = (left + right)//2
                if numbers[middle] == temp:
                    return [idx+1, middle+1]
                elif numbers[middle] > temp:
                    right = middle -1
                else:
                    left = middle + 1
        return []