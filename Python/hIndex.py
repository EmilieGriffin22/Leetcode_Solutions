#Original correct but inefficient solution, as it relies on 
#sorting, which is O(nlogn)
def hIndex(self, citations):
    citations.sort() 
    hIndex = 0
    for i in range(len(citations)): 
        left = len(citations) - i
        if (left >= citations[i]): 
            hIndex = citations[i]
        elif (left > hIndex): 
            hIndex = left
    return hIndex 

#Optimized solution dervied from above: 
def hIndex(self, citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= (len(citations) - i):
            return len(citations) - i
    return 0

#Optimized solution for time (uses extra space): 
def hIndex(self, citations):
    #The value of hIndex can never be more than the length of the array. 
    citation_counts = [0] * (len(citations) + 1)
    for i in range(len(citations)): 
        if (citations[i] < len(citations)): 
            citation_counts[citations[i]] += 1 
        else: 
            citation_counts[len(citations)] += 1 
    count = 0
    for i in range(len(citations), -1, -1): 
        count += citation_counts[i]
        if (i <= count): 
            return i