def summaryRanges(self, nums):
    ret = [] 
    i = 0
    while i < len(nums): 
        endRange = i 
        while endRange + 1 < len(nums) and nums[endRange+1] == nums[endRange] + 1: 
            endRange+= 1
        if (endRange - i >= 1): 
            ret.append(str(nums[i]) + "->" + str(nums[endRange]))
        else: 
            ret.append(str(nums[i]))
        i = endRange + 1
    return ret 