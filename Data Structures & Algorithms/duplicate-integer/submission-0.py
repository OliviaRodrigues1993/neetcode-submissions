class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for each_value in nums:
            #print(each_value)
            count[each_value] = count.get(each_value,0)+1
        for c in count.values():
            if c > 1:
                return True
             
        return False
        

        

        