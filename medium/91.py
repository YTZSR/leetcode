class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        length = len(s)
        solution = [1]
        ans = 0
        for i in range(length - 1, -1, -1):
            
            if s[i] == '0':
                solution.append(0)
                continue
            
            if i == length - 1:
                solution.append(1)
                continue
            
            ans = solution[length - 1 - i]
            if int(s[i:i + 2]) <= 26:
                ans += solution[length - 2 - i]

            solution.append(ans)

        return solution[-1]
            
            

            