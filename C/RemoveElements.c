//Original correct solution. 
int removeElement(int* nums, int numsSize, int val) {
    int k = numsSize; 
    int end = numsSize - 1; 
    int i = 0; 
    while(i < end){
        if(nums[i] == val){
            k--; 
            nums[i] = nums[end--]; 
        } else {
            i++; 
        }
    }

    if(numsSize > 0 && nums[i] == val){
        k--;
    }

    return k; 
    
}

//Optimized correct solution, removed unessecary variables. 
int removeElement(int* nums, int numsSize, int val) {
    int i = 0; 
    while(i <= (numsSize - 1)){
        if(nums[i] == val){
            nums[i] = nums[(numsSize--) - 1]; 
        } else {
            i++; 
        }
    }

    if(i < numsSize && nums[i] == val){
        numsSize--;
    }

    return numsSize; 
}

//Alternate approach: copying array for elements that are not val. 
int removeElement(int* nums, int numsSize, int val) {
    int k = 0;
    for (int i = 0; i < numsSize; i++){
        if(nums[i] != val){
            nums[k] = nums[i]; 
            k++; 
        }
    }
    return k; 
}
