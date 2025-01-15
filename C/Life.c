//Original correct and efficient solution, although not very pretty.
//Neighbor computation could be another method, but that would use *slightly* more memory. 
void gameOfLife(int** board, int boardSize, int* boardColSize) {
    //Idea: To compute in place, use the second bit of the integer to represent the next state. 
    for (int i = 0; i < boardSize; i++){
        for (int j = 0; j < boardColSize[i]; j++) {
            int liveNeighbors = 0; 
            //0
            if ((i - 1) >= 0 && (j - 1) >= 0 && (board[i-1][j-1] & 1)){
                liveNeighbors++; 
            }

            //1
            if ((i - 1) >= 0 && (board[i - 1][j] & 1)){
                liveNeighbors++; 
            }

            //2
            if ((i - 1) >= 0 && (j + 1) < boardColSize[i] && (board[i-1][j+1] & 1)){
                liveNeighbors++; 
            }

            //3
            if ((j - 1) >= 0 && (board[i][j-1] & 1)){
                liveNeighbors++; 
            }

            //4
            if ((j + 1) < boardColSize[i] && (board[i][j+1] & 1)){
                liveNeighbors++; 
            }

            
            if ((i + 1) < boardSize && (j - 1) >= 0 && (board[i + 1][j-1] & 1)){
                liveNeighbors++; 
            }

            //6
            if ((i + 1) < boardSize && (board[i+1][j] & 1)){
                liveNeighbors++; 
            }

            //7
            if ((i + 1) < boardSize && (j + 1) < boardColSize[i] && (board[i+1][j+1] & 1)){
                liveNeighbors++; 
            }
            
            if ((board[i][j] & 1) && (liveNeighbors == 2 || liveNeighbors == 3)){
                board[i][j] = board[i][j] | 0x2; 
            } else if (!(board[i][j] & 1) && (liveNeighbors == 3)){
                board[i][j] = board[i][j] | 0x2; 
            } 

        }
    }


    for (int i = 0; i < boardSize; i++){
        for (int j = 0; j < boardColSize[i]; j++) {
            board[i][j] = board[i][j] & 0x2 && 1; 
        }
    }
}

