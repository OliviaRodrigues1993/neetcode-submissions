class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(len(s))
        print(len(t))

        if len(s) != len(t):
            return False

        first_count = {}
        second_count = {}

        for e in s:
            first_count[e] = (first_count.get(e,0)+1)
        for i in t:
            second_count[i] = (second_count.get(i,0)+1)

        return first_count == second_count
            

        #print(first_count)
        #print(second_count)
        

        

        
        
