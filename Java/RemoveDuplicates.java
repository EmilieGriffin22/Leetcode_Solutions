//Original correct solution, appears to be fully optimized (O(n) time complexity, O(1) space complexity -- just two integers are created)
public int removeDuplicates(int[] nums) {
        int p1 = 0; 
        int p2 = 0; 
        while (p2 < nums.length - 1){
            if(nums[p2] != nums[p2 + 1]){ //Last copy found.
                nums[p1] = nums[p2]; 
                p1++; 
            }
            p2++;
        }

        nums[p1] = nums[p2]; 
        return p1 + 1; 
    
}