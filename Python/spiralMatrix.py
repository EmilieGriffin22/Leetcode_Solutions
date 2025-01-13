#Original correct solution (time + space efficient). 
def spiralOrder(self, matrix):
    # Pattern is inherently: increase j, increase i, decrease j, decrease i each time until a "wall" is hit. 
    spiral = [0] * len(matrix) * len(matrix[0])
    i = 0
    j = 0 
    k = 0 
    state = 1 
    
    while (k < len(spiral)): #While there is more to place. 
        spiral[k] = matrix[i][j] 
        matrix[i][j] = None
        if state == 1:
            if j + 1 >= len(matrix[0]) or matrix[i][j + 1] is None: 
                state = 2
                i += 1
            else: 
                j += 1  
        elif state == 2: 
            if i + 1 >= len(matrix) or matrix[i+1][j] is None: 
                state = 3
                j -= 1
            else: 
                i += 1 
        elif state == 3: 
            if j - 1 < 0 or matrix[i][j - 1] is None:
                state = 4 
                i -= 1
            else: 
                j -= 1 
        else: 
            if i - 1 < 0 or matrix[i-1][j] is None: 
                state = 1
                j += 1 
            else: 
                i -= 1 

        k += 1
    return spiral 

