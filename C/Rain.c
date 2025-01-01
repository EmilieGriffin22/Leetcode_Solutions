//Original correct solution (optimal)
int trap(int* height, int heightSize) {
    int water = 0; 
    int left = 0; 
    int right = heightSize; 
    int leftMax = height[left]; 
    int rightMax = height[right]; 

    while (left < right) {
        if (leftMax < rightMax) {
            if (height[left] > leftMax){
                leftMax = height[left]
            }
            left++; 
            water += leftMax - height[left]; 
        } else {
            if (height[right] > rightMax) {
                rightMax = height[right]; 
            }
            right++; 
            water += rightMax - height[right]; 
        }
    }

    return water; 
}