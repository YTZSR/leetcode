class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 1
        direction = True
        power = 0
        while n != 1:
            if direction == True:
                ans += pow(2, power)
                direction = False
            else:
                if n % 2 == 1:
                    ans += pow(2, power)
                direction = True
                
            power += 1
            n = int(n/2)

        return ans
