//Original correct solution. 
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int temp[m+n]; 
    int pointer1 = 0;
    int pointer2 = 0;
    int i = 0; 
    while(pointer1 < m && pointer2 < n){
        if (nums1[pointer1] <= nums2[pointer2]){
                temp[i] = nums1[pointer1]; 
                pointer1++; 
        } else {
            temp[i] = nums2[pointer2]; 
            pointer2++;
        }
        i++;
    }

    while(pointer2 < n){
        temp[i] = nums2[pointer2]; 
        pointer2++;
        i++;
    }

    while(pointer1 < m){
        temp[i] = nums1[pointer1]; 
        pointer1++;
        i++;
    }

    for (int j = 0; j < m + n; j++)
        nums1[j] = temp[j];    
}

//Optimized correct solution, performs the change in place. 
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int pointer1 = m - 1; 
    int pointer2 = n - 1; 
    int finalPlace = m + n - 1; 

    while(pointer2 >= 0){ //Where there are still elements in nums2 to be inserted. 
        if(pointer1 >= 0 && nums1[pointer1] > nums2[pointer2]){ 
            nums1[finalPlace--] = nums1[pointer1--]; 
        } else {
            nums1[finalPlace--] = nums2[pointer2--]; 
        }

    }
}