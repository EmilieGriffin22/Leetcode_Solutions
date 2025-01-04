#Orignial correct and time efficient solution. 
def convert(self, s, numRows):
    if(numRows == 1): 
        return s 
    numRows -= 1 
    r = 0 
    ascending = True 
    indices = [""] * (numRows + 1)
    for i in range(len(s)): 
        indices[r] += s[i] 
        if r == numRows: 
            ascending = False 
        elif r == 0: 
            ascending = True 
        if ascending: 
            r += 1 
        else:  
            r -= 1 
    s = ""
    for i in indices: 
        s += i
    return s