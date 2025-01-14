//Original corrct + efficient solution. 
public void rotate(int[][] matrix) {
    //A rotation about the origin of 90 degrees traditionally maps: (x, y) -> (y, -x). 
    //The transpose of a matrix: (x, y) --> (y, x) 
    //Reversing a row: (x, y) --> (-x, y)

    //First, do the transpose. 
    for (int i = 0; i < matrix.length; i++){
        for (int j = i; j < matrix[i].length; j++){
            int temp = matrix[j][i]; 
            matrix[j][i] = matrix[i][j]; 
            matrix[i][j] = temp; 
        }
    }

    //Reverse each row. 
    for (int i = 0; i < matrix.length; i++){
        for (int j = 0; j < matrix[i].length / 2; j++){
            int temp = matrix[i][j]; 
            matrix[i][j] = matrix[i][matrix[i].length - j - 1]; 
            matrix[i][matrix[i].length - j - 1] = temp; 
        }
    }
}
