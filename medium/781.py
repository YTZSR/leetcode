class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        i = 0
        ans = 0
        while i < len(answers):
            num = answers[i]
            count = 1
            while i + 1< len(answers) and answers[i + 1] == num:
                count += 1
                i += 1
            ans += int(count / (num + 1)) * (num + 1)
            if count % (num + 1) > 0:
                ans += num + 1
            i += 1
        return ans
            
            