//O(n) solution. 
public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> mapping = new HashMap<>(); 
    for (int i = 0; i < nums.length; i++){
        int temp = mapping.getOrDefault(target - nums[i], -1);
        if (temp != -1 && temp != i){
            return new int[]{i, temp}; 
        }
        mapping.put(nums[i], i);
    }
    return new int[]{};  
}

//O(n^2) solution. 
public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++){
        for (int j = i + 1; j < nums.length; j++){
            if (nums[i] + nums[j] == target){
                return new int[]{i, j}; 
            }

        }
    }
    return new int[]{};
}