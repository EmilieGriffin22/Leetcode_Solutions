public int[] twoSum(int[] numbers, int target) {
    int p1 = 0; 
    int p2 = numbers.length - 1; 
    int answer[] = {0, 0}; 

    while (p1 < p2){
        if (numbers[p1] + numbers[p2] == target){
            answer[0] = p1 + 1;
            answer[1] = p2 + 1;
            return answer; 
        } else if (numbers[p1] + numbers[p2] > target){
            p2--; 
        } else {
            p1++; 
        }
    }
    return answer;  
}