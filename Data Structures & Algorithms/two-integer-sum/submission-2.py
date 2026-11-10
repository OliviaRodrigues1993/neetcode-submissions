class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                   result = nums[i]+nums[j]
                   #print(result)
                   if result == target:
                    return [i,j]
        


        