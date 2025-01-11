#Original correct and time-efficient solution.
def wordPattern(self, pattern, s):
    words = s.split() 
    pattern_to_s = {} 
    s_to_pattern = set() 
    if len(pattern) != len(words): 
        return False 
    for i in range(len(pattern)): 
        if pattern[i] not in pattern_to_s: 
            pattern_to_s[pattern[i]] = words[i]
            if words[i] in s_to_pattern: 
                return False 
            s_to_pattern.add(words[i])
        elif pattern_to_s[pattern[i]] != words[i]: 
            return False 
    return True 
