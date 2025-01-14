//Original correct and memory complexity efficient solution (uses O(1) space and beats ~60% of other solutions). 
void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    bool firstRowZero = false; 
    bool firstColZero = false; 

    for (int i = 0; i < matrixSize; i++){
        for (int j = 0; j < matrixColSize[i]; j++){
            if (!matrix[i][j]){
                if (i == 0) {firstRowZero = true;}; 
                if (j == 0) {firstColZero = true;};
                matrix[i][0] = 0; 
                matrix[0][j] = 0; 
            }
        }
    }

    for (int i = 1; i < matrixSize; i++){
        for (int j = 1; j < matrixColSize[i]; j++){
            if (!matrix[i][0] || !matrix[0][j]){
                matrix[i][j] = 0; 
            }
        }
    }

    if (firstRowZero){
        for (int j = 0; j < matrixColSize[0]; j++){
            matrix[0][j] = 0; 
        }

    }

    if (firstColZero){
        for (int i = 0; i < matrixSize; i++){
            matrix[i][0] = 0; 
        }

    }
}