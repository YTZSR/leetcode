class Solution:
    def sortString(self, s: str) -> str:
        arr = list(s)
        arr.sort()
        ans = []
        while len(arr) > 0:

            current = ''
            i = 0
            while i < len(arr):
                if current != arr[i]:
                    current = arr[i]
                    ans.append(current)
                    arr.remove(arr[i])
                else:
                    i += 1
            i = len(arr) - 1
            current = ''
            while i >= 0:
                if current != arr[i]:
                    current = arr[i]
                    ans.append(current)
                    arr.remove(arr[i])
                i -= 1
        return ''.join(ans)
        
            