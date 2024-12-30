#Original correct solution 
#Note: Although it technically doesn't use division as required, 
#I still think of this as "cheating" due to its use of the negative power. 
def productExceptSelf(self, nums):
    answer = [0] * len(nums)
    totalprod = 1 
    totalprodnozeros = 1 
    zerocount = 0 
    for i in nums: 
        totalprod *= i 
        if i != 0: 
            totalprodnozeros *= i 
        if (i == 0): 
            zerocount+=1
    
    #Now, how to do division by nums[i] WITHOUT division? 
    #Raise to negative power? 
    #But what about 0s? 
    for i in range(len(answer)): 
        if (nums[i] != 0): 
            answer[i] = int((totalprod) * (nums[i]**-1))
        elif (zerocount == 1): 
            answer[i] = totalprodnozeros
    return answer 

#Slighlty better, but still O(n) space
def productExceptSelf(self, nums):
    #okay, we can do better 
    prefix = [1] * len(nums)
    for i in range(1, len(prefix)): 
        prefix[i] = nums[i - 1] * prefix[i - 1]

    suffix = [1] * len(nums) 
    for i in range(len(suffix) - 2, -1, -1): 
        suffix[i] = nums[i+1] * suffix[i+1]

    answer = [0] * len(nums)
    for i in range(len(suffix)): 
        answer[i] = prefix[i] * suffix[i]
    return answer

#Optimized 
def productExceptSelf(self, nums):
    answer = [1] * len(nums)
    for i in range(1, len(answer)): 
        answer[i] = nums[i - 1] * answer[i - 1]


    suffix = 1
    for i in range(len(answer) - 1, -1, -1): 
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
        