class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalnum():
                result+=i.lower()
        
        print(result)
        print(result[::-1])
        return result == result[::-1]
         
        