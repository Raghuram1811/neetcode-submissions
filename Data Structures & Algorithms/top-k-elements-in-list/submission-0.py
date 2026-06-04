class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        check, response = dict(), []
        for num in nums:
            check[num] = check.get(num, 0)+1
        
        check = dict(sorted(check.items(), key=lambda item: item[1], reverse=True))

        for key in check.keys():
            response.append(key)
            k-=1
            if k==0:
                break
        return response

        