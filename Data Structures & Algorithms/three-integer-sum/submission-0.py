class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        total = 0
        nums.sort()

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            if nums[i]==nums[i-1] and i!=0:
                continue
            
            while left< right:
                total = nums[i]+nums[left] +nums[right]

                if total <0:
                    left +=1
                elif total >0:
                    right -=1
                else:
                    output.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1

                    while left<right and nums[left] == nums[left - 1]:
                        left +=1
        return output


        