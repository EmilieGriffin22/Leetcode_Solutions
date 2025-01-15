#Original correct solution, but so inefficient that it times out: 
def groupAnagrams(self, strs):
    output = []
    for word in strs: 
        added = False 
        s = sorted(word)
        for group in output: 
            if s == sorted(group[0]): 
                group.append(word)
                added = True 
        if not added: 
            output.append([word])
    return output 


#Imrpovement on above solution that is conceptually the same, but FAR more efficient. 
def groupAnagrams(self, strs):
    output = []
    dic = {} 


    for word in strs: 
        s = ''.join(sorted(word))
        if s in dic: 
            dic[s].append(word)
        else: 
            dic[s] = [word]
        
    for key in dic: 
        output.append(dic[key])
    return output 