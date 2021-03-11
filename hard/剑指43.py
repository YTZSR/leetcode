class Solution:
    def countDigitOne(self, n: int) -> int:
        def complete(n: int) -> int:
            i = 1
            ans = 0
            while i <= n:
                ans = ans * 10 + pow(10, i-1)
                i += 1
            return ans

        if n < 10:
            if n == 0:
                return 0
            else:
                return 1
        first = int(str(n)[0])
        if first > 1:
            return pow(10,len(str(n)) - 1) + complete(len(str(n)) - 1) * first + self.countDigitOne(int(str(n)[1:]))
        else:
            return int(str(n)[1:]) + 1 + complete(len(str(n)) - 1) + self.countDigitOne(int(str(n)[1:]))

    