//Original correct (and very efficient) solution. 
bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    int validRows[9] = {0}; 
    int validColumns[9] = {0}; 
    int validBoxes[9] = {0}; 

    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            if (board[i][j] == '.') {continue;}; 
            int num = 1 << (board[i][j] - '0'); 

            //Check the rows. 
            if (validRows[i] & num){
                return false; 
            } else {
                validRows[i] = validRows[i] | num; 
            }

            //Check the coumns.
            if (validColumns[j] & num){
                return false; 
            } else {
                validColumns[j] = validColumns[j] | num; 
            }

            //Check the box. 
            int box = (i / 3) * 3 + (j / 3); 

            if (validBoxes[box] & num){
                return false; 
            } else {
                validBoxes[box] = validBoxes[box] | num;
            }
        }
    }
    return true; 
}