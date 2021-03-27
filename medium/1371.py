class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        table = 0
        loc = {}
        loc[0] = 0
        ans = 0

        for i in range(len(list(s)) ):
            if s[i] == 'a':
                table = table ^ (1 << 4)
            elif s[i] == 'e':
                table = table ^ (1 << 3)
            elif s[i] == 'i':
                table = table ^ (1 << 2)
            elif s[i] == 'o':
                table = table ^ (1 << 1)
            elif s[i] == 'u':
                table = table ^ 1

            if table in loc:
                ans = max(ans, i + 1 - loc[table])
            else:
                loc[table] = i + 1
            print(ans)
        
        return ans