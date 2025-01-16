# Solution that is better for runtime (original solution). 
def containsNearbyDuplicate(self, nums, k):
    mapping = {} 
    for i in range(len(nums)): 
        if nums[i] in mapping and abs(mapping.get(nums[i]) - i) <= k: 
            return True 
        else: 
            mapping[nums[i]] = i
    return False 


# Better for memory.
def containsNearbyDuplicate(self, nums, k): 
    s = set() 
    for i in range(len(nums)): 
        if nums[i] in s: 
            return True 
        s.add(nums[i])
        if i - k >= 0: 
            s.remove(nums[i -k])
    return False 