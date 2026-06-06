class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # middle = len(numbers)//2

        # if numbers[middle] >= target:
        #     self.twoSum(numbers[:middle], target)
        
        for idx in range(len(numbers)):
            left, right = idx+1, len(numbers)-1

            temp = target - numbers[idx]
            while left<=right:
                mid = (left+right)//2
                if numbers[mid] == temp:
                    return [idx+1, mid+1]
                elif numbers[mid] < temp:
                    left = mid+1
                else:
                    right = mid-1
        return []