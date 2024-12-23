//Original correct solution
public int removeDuplicates(int[] nums) {
        if(nums.length <= 2){
            return nums.length; 
        }

        int p1 = 1; 
        int p2 = 1; 
        while (p2 < nums.length - 1){
            if(nums[p2] != nums[p2 + 1] || nums[p2] != nums[p2 - 1]){
                nums[p1] = nums[p2]; 
                p1++; 
            }
            p2++;
        }

        nums[p1] = nums[p2]; 
        return p1 + 1; 
}

//Slightly better solution, removes extra check at beginning. 
public int removeDuplicates(int[] nums) {
        int p1 = 2; 
        int p2 = 2; 
        while (p2 < nums.length){
            if(nums[p2] != nums[p1 - 2]){
                nums[p1] = nums[p2]; 
                p1++; 
            }
            p2++;
        }
        return p1; 
}