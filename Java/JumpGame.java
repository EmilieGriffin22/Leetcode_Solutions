//Original correct solution -- not very elegant, reminiscent of Frankenstein. 
public boolean canJump(int[] nums) {
        int target = nums.length - 1; 
        int curr = 0;  
        while (curr < target) {
            int step = nums[curr]; 
            if (curr + step >= target){
                return true; 
            }
            while(nums[curr + step] == 0){
                step--; 
                if(curr + step < 0){
                    return false; 
                }
                if(nums[curr + step] == -1){
                    step--;
                    if(curr + step < 0){
                    return false; 
                }
                }
            }

            if (curr + step == 0) {
                return false; 
            } else {
                nums[curr] = -1;
                curr += step; 
            }
        }
        return true; 
    }


//Optimized solution (greedy). 
public boolean canJump(int[] nums) {
        int best = 0; 
        int curr = 0; 
        int target = nums.length - 1; 
        while (curr <= target){ //While we haven't considered every array element. 
            if(curr > best) { //If our current element is unreachable. 
                return false; 
            }  
            if (curr + nums[curr] > best) { //If we can go farther than we previously thought.
                best = curr + nums[curr];  
            }
            if (best >= target){ //If we've gone far enough.
                return true; 
            }
            curr++;
        }
        return false; 
}

//Even better solution, made by moving a "goal"
//Solution by Leetcode user: niits (used for studying optimal solution)
public boolean canJump(int[] nums) {
        int goal = nums.length - 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }

        return goal == 0;        
}


