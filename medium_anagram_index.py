
text = 'abab'
p = 'ab'

def char_dec(text):
    counts = {}
    for c in set(text):
        counts[c] = text.count(c)
    return(counts)

p_len = len(p)
d = char_dec(p)

res = list()
for i in range(len(text)):
    if d == char_dec(text[i:p_len+i]): 
        res.append(i)

print(res)


# leetcode submission -  slow due to O(n^2)
class Solution:
    from collections import Counter
    
    def char_dec(self, text):
        counts = {}
        for c in set(text):
            counts[c] = text.count(c)
        return(counts)

    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = list()
        p_len = len(p)
        d = Counter(p)
        for i in range(len(s)):
            if d == Counter(s[i:p_len+i]): 
                res.append(i)
        return(res)
        