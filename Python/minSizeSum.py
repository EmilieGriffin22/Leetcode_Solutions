#Original correct but inefficient solution.
def minSubArrayLen(self, target, nums):
    if sum(nums) < target: 
        return 0 
    
    s = 0
    best = len(nums)
    end = 0 
    for start in range(len(nums)): 
        while s < target and end < len(nums): 
            s += nums[end]
            end += 1 
        if s >= target and end - start < best: 
            best = end - start 
        s -= nums[start]
    return best 

#Far more time efficient solution. 
def minSubArrayLen(self, target, nums):
    s = 0
    best = len(nums) + 1
    start = 0 
    for end in range(len(nums)): 
        s += nums[end]
        while s >= target: 
            if (end - start + 1) < best: 
                best = end - start + 1
            s -= nums[start]
            start += 1 
    return best if best <= len(nums) else 0