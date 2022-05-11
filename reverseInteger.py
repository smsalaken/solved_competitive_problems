class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        x_c = str(abs(x))
        x_s = ""
        lim = len(x_c)
        for i in range(len(x_c)) :
            x_s = x_s + x_c[lim-i-1]
        res = sign*int(x_s)
            
        if (abs(res) > (2**31-1)):
            return(0)
        else:
            return(res)