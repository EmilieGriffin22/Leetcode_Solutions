#Original correct but inefficient solution. 
def lengthOfLongestSubstring(self, s):
    longest = 0  
    end = 0
    seen = {}
    for start in range(len(s)): 
        while end < len(s) and seen.get(s[end], 0) == 0: 
            if (end - start + 1) > longest: 
                longest = end - start + 1
            seen[s[end]] = 1 
            end += 1 
        seen[s[start]] = 0
    return longest 

#More efficient, but far from perfect solution
def lengthOfLongestSubstring(self, s):
    longest = 0  
    start = 0 
    seen = set()
    for end in range(len(s)): 
        while s[end] in seen: 
            seen.remove(s[start]) 
            start += 1
        seen.add(s[end])
        if end - start + 1 > longest: 
            longest = end - start + 1 
    return longest 

#Even better.
def lengthOfLongestSubstring(self, s):
    longest = 0
    start = 0
    lastseen = {}
    for end in range(len(s)): 
        val = lastseen.get(s[end], -1)
        if val >= start: 
            start = val + 1
        longest = max(longest, end - start + 1)
        lastseen[s[end]] = end 
    return longest