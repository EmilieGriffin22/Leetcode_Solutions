    //Original correct but inefficient solution. 
    public int jump(int[] nums) {
        //Take the farthest back that can hit the target and then update it? 
        int target = nums.length - 1; 
        int steps = 0; 
        while (target > 0){
            int farthest = target; 
            for (int i = 0; i < target; i++){
                if (i + nums[i] >= target && i <= farthest){
                    farthest = i; 
                }
            }

            target = farthest; 
            steps++; 
            
        }
        return steps; 
    }

    //Better solution: O(n) 
    //Greedy.
    public int jump(int[] nums) {
        int step = 0; 
        int farthest = 0; 
        int range = 0; 
        for (int i = 0; i < nums.length - 1; i++){ //nums.length - 1 is the targest element. 
            if (nums[i] + i > farthest) { //If we start at element i, is the furthest we can go farther than any other element in our range? 
                farthest = nums[i] + i; //If yes, update farhtest. 
            }

            if (i == range){ //If we've hit the end of our range. 
                range = farthest; //Update our new range, i.e. where we're going, to be the farthest we could go. 
                step++; //Take that as a step. 
            }
        }
        return step; 
    }
