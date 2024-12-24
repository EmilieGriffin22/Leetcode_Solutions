#Initial correct (but ineffiicent) solution 
#Uses O(n) time but also O(n) space. 
def rotate(self, nums: List[int], k: int) -> None:
        #new spot: (current_index + k) % n
        #the problem: it's not just a simple swap with that element. 
        temp = []
        for i in range(len(nums)): 
            temp.append(nums[i])

        for i in range(len(nums)): 
            new_index = int((i + k) % len(nums))
            temp[new_index] = nums[i]

        for i in range(len(nums)): 
            nums[i] = temp[i]

#Better solution with O(1) extra space and still O(n) time. 
def rotate(self, nums: List[int], k: int) -> None:
    k = k % len(nums)
    if k == 0: 
        return

    #Reverse the array.
    for i in range(int(len(nums) / 2)): 
        temp = nums[len(nums) - i - 1]
        nums[len(nums) - i - 1] = nums[i]
        nums[i] = temp 

    #Reverse the first portion. 
    for i in range(int(k / 2)): 
        temp = nums[k - i - 1]
        nums[k - i - 1] = nums[i]
        nums[i] = temp

    #Reverse the second portion. 
    for i in range(0, int((len(nums) - k) / 2)): 
        temp = nums[len(nums) - i - 1]
        nums[len(nums) - i - 1] = nums[k + i]
        nums[k + i] = temp

#The above solution, but using built-in Python behavior for efficiency. 
def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0: 
            return
        nums.reverse() 
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])