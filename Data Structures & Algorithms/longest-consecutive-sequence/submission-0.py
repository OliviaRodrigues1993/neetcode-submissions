class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        print("numset=",numset)
        max_len = 0

        for each_num in nums:
            #print("each_num=",each_num)
            if each_num-1 not in numset:
                #print("each_num-1",each_num-1)
                current_number = each_num
                current_len = 1
                while current_number+1 in numset:
                    #print("current_number+1",current_number+1)
                    #print("current_number start",max_len)
                    #print("current_len start",current_len)
                    current_len+=1
                    current_number+=1 #increment by 1 seq
                    #print("current_number last",max_len)
                    #print("current_len last2=",current_len)
                max_len= max(current_len,max_len)
                #print("max_len=",max_len)



        return max_len