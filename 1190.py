class Solution(object):
    def isPalindrome(self, s):
        def isValid(char):
            if 'Z' >= char >= 'A' or 'z' >= char >= 'a' or '9' >= char >= '0':
                return True
            return False
        
        i = 0
        j = len(s) - 1
        while(i < j):
            if not isValid(s[i]):
                i +- 1
            elif not isValid(s[j]):
                j -= 1
                
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
    