#Original correct and optimized (in terms of complexity classes) solution.
def threeSum(self, nums):
    out = [] 
    nums.sort() 
    print(nums)
    for p1 in range(len(nums)):
        if p1 != 0 and nums[p1] == nums[p1 - 1]: 
            continue 
        p2 = p1 + 1 
        p3 = len(nums) - 1 
        while p2 < p3: 
            s = nums[p1] + nums[p2] + nums[p3]
            if s > 0: 
                p3 -= 1 
            elif s < 0: 
                p2 += 1 
            else: 
                out.append([nums[p1], nums[p2], nums[p3]]) 
                p2 += 1 
                while p2 < p3 and nums[p2 - 1] == nums[p2]: 
                    p2+=1
    return out 