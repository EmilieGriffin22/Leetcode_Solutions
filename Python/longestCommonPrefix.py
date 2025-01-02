#Original correct solution.
def longestCommonPrefix(self, strs):
    ret = strs[0]
    for i in range(1, len(strs)): 
        word = strs[i]
        lew = len(word)
        if len(ret) > lew: 
            ret = ret[0:lew]
        elif len(ret) < lew: 
            word = word[0:len(ret)]

        lew = len(word) - 1
        while lew >= 0: 
            if (word[lew] != ret[lew]): 
                ret = ret[0:lew]
            lew -= 1
    return ret 


#Same logic, but more efficient. 
#Complecity: O(S), where S is the summed length of all strings in strs. 
#This is nessecary as each character in strs must be considered. 
def longestCommonPrefix(self, strs):
    ret = strs[0]
    for s in strs[1:]: 
        while not s.startswith(ret): 
            ret = ret[:-1]
            if ret == "" :
                return ret
    return ret 