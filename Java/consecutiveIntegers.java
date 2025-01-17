public int longestConsecutive(int[] nums) {
    HashSet<Integer> set = new HashSet<>(); 
    for (int i :nums){
        set.add(i);
    }

    int max = 0; 
    for (int i : set){
        if (!set.contains(i - 1)){
            int currMax = 1; 
            while (set.contains(i + currMax)){
                currMax++; 
            }
            max = Math.max(currMax, max); 
        }
    }

    return max; 
    
}