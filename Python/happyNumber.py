#Original efficient solution.
def isHappy(self, n):
    seen = set()
    while n not in seen: 
        seen.add(n)
        s = 0
        while n > 0: 
            s += ((n % 10) ** 2) 
            n /= 10
        if s == 1: 
            return True 
        n = s
    return False 