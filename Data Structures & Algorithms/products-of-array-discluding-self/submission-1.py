class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            results = 1
            for j in range(len(nums)):
                
                if i!=j:
                    #print("i=",i)
                    #print("j=",j)
                    results *=nums[j]
            output.append(results)

        return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        left_array = [0]*n
        #print("left_array",left_array)
        right_array = [0]*n
        #print("right array=",right_array)
        
        #print("n=",n)
        left_array[0]=1
        for i in range(1,n):
            
            left_array[i] = nums[i-1]*left_array[i-1]
        #print("left_array=",left_array)

        right_array[n-1] = 1

        for j in range(n-2,-1,-1):
            #print("j=",j)
            #print("right_array[j]=",right_array[j])
            #print("nums[j+1]=",nums[j+1])
            #print("right_array[j+1]=",right_array[j+1])
            right_array[j] = nums[j+1]*right_array[j+1]
            #print("right_array=",right_array)
        for i in  range(n):
            output.append(left_array[i]*right_array[i])            

        

        return output
    



        