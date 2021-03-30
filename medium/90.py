class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        hashList = []

        for i in range(pow(2,len(nums))):
            temp = i
            tempList = []
            for index in range(len(nums)):
                if temp % 2 == 1:
                    tempList.append(nums[index])
                temp = int(temp / 2)
            tempList.sort()
            if hash(str(tempList)) not in hashList:
                ans.append(tempList)
                hashList.append(hash(str(tempList)))
        return ans