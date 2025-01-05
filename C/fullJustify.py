#A VERY inefficient solution, but my first solution none-the-less.
def fullJustify(self, words, maxWidth):
    #First, we need to figure out what words will go on what line. 
    lines = [] 
    i = 0 
    while i < len(words):
        line = []
        line_len = 0 
        while i < len(words) and (line_len + len(words[i])) <= maxWidth: 
            line.append(words[i] + " ")
            line_len += len(words[i]) + 1
            i += 1 
        line[-1] = line[-1][:-1]
        line.append(line_len - 1)
        lines.append(line)
    
    #Okay, now to add in the extra spaces. 
    for i in range(len(lines)): 
        diff = maxWidth - lines[i][-1]
        lines[i] = lines[i][:-1]
        if i == len(lines) - 1 or len(lines[i]) == 1: #The last line or a line with one word. 
            while diff > 0: 
                lines[i][-1] += " "
                diff -= 1
        else: #The line has more than one word and its not the last line. 
            extra_spaces_per_space = diff / (len(lines[i]) - 1) #How many extra spaces will EVERY space be assigned?
            more_spaces_needed = diff - (extra_spaces_per_space * (len(lines[i]) - 1))
            for j in range(len(lines[i]) - 1): 
                for p in range(extra_spaces_per_space): 
                    lines[i][j] += " "
                while more_spaces_needed > 0: 
                    for lw in range(len(lines[i]) - 2): 
                        if more_spaces_needed > 0: 
                            lines[i][lw] += " "
                            more_spaces_needed -= 1

    for i in range(len(lines)):  
        newline = ""
        for j in range(len(lines[i])): 
            newline += lines[i][j]
        lines[i] = newline

    return lines


#Better Solution: Removes some loops and unessecary variables. 
#Time complexity: O(N)
#Space complexity: O(N)
def fullJustify(self, words, maxWidth):
    #First, we need to figure out what words will go on what line. 
    lines = [] 
    i = 0 
    while i < len(words): #Each word in words will be consdiered once -> O(N)
        line = []
        line_len = 0 
        while i < len(words) and (line_len + len(words[i])) <= maxWidth: 
            line.append(words[i] + " ")
            line_len += len(words[i]) + 1
            i += 1 
        line[-1] = line[-1][:-1]
        #Add the extra spaces. 
        diff = maxWidth - (line_len - 1)
        if i == len(words) or len(line) == 1: #The last line or a line with one word. 
            line.append(' ' * diff)
        else: 
            extra_spaces_per_space = diff // (len(line) - 1)
            more_spaces_needed = diff % (len(line) - 1)
            for j in range(len(line) - 1): #Len(line) is a constant, as it must be <= maxWidth. Whole loop is therefore O(1). 
                line[j] += " " * extra_spaces_per_space
                if more_spaces_needed > 0: 
                    line[j] += " "
                    more_spaces_needed -= 1 #Will never need to give a word more than one extra space. 
        lines.append("".join(line))
    return lines