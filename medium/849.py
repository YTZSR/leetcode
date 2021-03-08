class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index = 0
        ans = 0
        temp = 0
        while seats[index] != 1:
            ans += 1
            index += 1

        index += 1
        while index < len(seats):
            if seats[index] != 1:
                temp += 1
                index += 1
            else:
                if (temp + 1)/ 2 > ans:
                    ans = int((temp + 1) / 2)
                temp = 0
                index += 1
        if temp > ans:
            ans = temp
        return ans
        
