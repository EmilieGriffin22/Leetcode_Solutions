#Initial correct (but inefficient) solution.
def majorityElement(self, nums: List[int]) -> int:
    freq = {}
    cap = len(nums) / 2
    for i in range(0, len(nums)): 
        freq[nums[i]] = freq.get(nums[i], 0) + 1
        if freq[nums[i]] >= cap: 
            return nums[i]
    
#Solution optimized for O(1) space and unqualified O(n) time. 
def majorityElement(self, nums: List[int]) -> int:
    p = -1 
    c = 0 
    for i in range(0, len(nums)): 
        if c == 0:     #For a majority element, c will never hit 0 unless the element appears again in the array.
                       #After all, all elements that are not the majority (!= p) must appear < n / 2 times, so the 
                       #Majority element can never have c decremented n / 2 times or more. Since it is initalized to 1
                       #The majority element will always end up with c > 0, since it appears n / 2 times or more. 
            p = nums[i]
            c = 1 
        else: 
            if nums[i] == p: 
                c +=1 
            else: 
                c -= 1 
    return p
