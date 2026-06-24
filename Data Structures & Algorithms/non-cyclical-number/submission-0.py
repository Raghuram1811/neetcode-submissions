class Solution:
    def isHappy(self, n: int) -> bool:

        if n==1:
            return True
        
        def f(x):
            digit, total = 0, 0
            while x!=0:
                digit = x%10
                total+=(digit**2)
                x=x//10
            return total
        
        hare, tort = n, n
        while True:

            hare = f(f(hare))
            tort = f(tort)
            if hare == 1:
                return True
            elif hare == tort:
                return False