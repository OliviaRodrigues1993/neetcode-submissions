class Solution:
    def isPalindrome2(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalnum():
                result+=i.lower()
        
        print(result)
        print(result[::-1])
        return result == result[::-1]

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right =len(s)-1

        while left < right:

            while left < right and not s[left].isalnum():
                left =left+1
            while left < right and not s[right].isalnum():
                right = right-1
            
            if s[left].lower() != s[right].lower() :
                return False
            left = left+1
            right=right-1
        return True

         
        