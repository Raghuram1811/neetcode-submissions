class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        def f(x):
            return nums[x]
        
        fast, slow = 0, 0
        while True:
            fast = f(f(fast))
            slow = f(slow)

            if fast == slow:

                slow2 = 0
                while slow2!=slow:
                    slow2 = f(slow2)
                    slow = f(slow)
                return slow
        return -1