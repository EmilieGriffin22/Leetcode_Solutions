#Original correct solutionL O(n) time and O(1) space. 
def lengthOfLastWord(self, s):
    ret = 0
    seenNon = False 
    for i in range(len(s) - 1, -1, -1): 
        if s[i] != ' ':
            ret += 1
            seenNon = True 
        elif seenNon: 
            return ret 
    return ret

#Another solution which takes advantage of Python 
def lengthOfLastWord(self, s):
    return len(s.split()[-1])